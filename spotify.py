import spotipy, os, json
import spotipy.util as util 
from spotipy.oauth2 import SpotifyClientCredentials


#Setting environment variables

os.environ["SPOTIPY_CLIENT_ID"] = "Get from spotify account"
os.environ["SPOTIPY_CLIENT_SECRET"] = "Get from spotify account"
os.environ["SPOTIPY_REDIRECT_URI"] = "https://google.com/"

scope = "user-read-private user-read-playback-state user-modify-playback-state" 
username = "UserName"

try:
    token = util.prompt_for_user_token(username, scope)
except:
    os.remove(f".cache = (username)")
    token = util.prompt_for_user_token(username, scope)
        
spotifyObj = spotipy.Spotify(auth = token)

    
def spot(userArtist, userSong):
    
    results = spotifyObj.current_user_playing_track()

    #If spotify is open 

    if results!=None:

        device = spotifyObj.devices()

        for i in range(0, len(device["devices"])):

            if (device["devices"][i]["is_active"])== True:

                deviceID = device["devices"][i]["id"]
        

        artistID = spotifyObj.search(userArtist, None, 0, "artist")

        artistInfo = artistID["artists"]["items"][0]

        artisturi = artistInfo["uri"]

        artistID = artistInfo["id"]
        
        tracks = spotifyObj.artist_top_tracks(artisturi, country = 'US')
        

        popularPlay = tracks["tracks"]
       
        popularJson = json.dumps(popularPlay, sort_keys = True, indent = 4)
        
        albums = spotifyObj.artist_albums(artistID)
        albums = albums["items"]
        
        for i in range(0, len(albums)):
            
            albumID = albums[i]["id"]
            songs = spotifyObj.album_tracks(albumID)
            
            
            songs = songs["items"]
            for every_song in songs:
                userSong = userSong.lower()
                userSong = removePunctuation(userSong)
                
                temp_change = every_song["name"]
                temp_change = temp_change.lower()
                temp_change = removePunctuation(temp_change)
                if (temp_change == userSong):
                    #start play back
                    trackUri = []
                    trackUri.append(every_song["uri"])
                    spotifyObj.start_playback(deviceID, None, trackUri)
                    return
                                        
    else:
        print("Please open spotify window.")
    



def removePunctuation(initWord):
    punctuations = ' !@#$%^&*()_-+=~`[]{};\':",.<>/?\|'
    changed = ""
    for every_char in initWord:
        if every_char not in punctuations:
            changed += every_char
        elif every_char =='(':          #Ignore anything after the name of the song "(Ft. XYZ)"
            return changed
    return changed

    
def get_input(someLine):
    tempSplit = someLine.split(",")
    artistName = tempSplit[0].strip()
    songName = tempSplit[1].strip()
    spot(artistName, songName)

