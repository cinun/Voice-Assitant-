import lyricsgenius
import first

def findLyrics(artistName, songTitle):
    """
    :param artistName: Self explanatory
    :param songTitle: The same
    :return: lyrics for the song of the first param
    """
    genius = lyricsgenius.Genius("Get key from genius.com")
    song = genius.search_song(songTitle, artistName)
    print(song.lyrics)
    


def main():
    findLyrics(a, b)


if __name__=="__main__":
    main()
