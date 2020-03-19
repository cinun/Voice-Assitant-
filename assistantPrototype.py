import cmd
import time
import weatherapi as weath
import openWebsite, jamesjokes, spotify
import lyricsFInder
import first
from sys import argv


class test(cmd.Cmd):
    """Simple command processor example"""
    
    def do_printargs(self, line):
        """
        print [Arguments]
        Given a terminal print the arguments
        """
        print("Your arguments are {}".format(line))
        first.playSound("randomxyz123.mp123") ## Can be anything you want
        
    def do_weather(self, line):
        """
        Given a location, prints the weather
        :param line: Is the command line argument that is given to us by the user.
        :return: The current weather at a location L
        """
        KEY = "Get key from openweatherapi"
        temp = weath.get_weather(KEY, line)
        printWeather = weath.printWeather(temp, weath.weather_dict, line)
        print(printWeather)
        first.mainSpeech(printWeather, "temp.mp3")
        first.playSound("temp.mp3")
        time.sleep(6)
        first.playSound("randomxyz123.mp123") ## Can be anything you want
        
    def do_createSong(self, line):
        '''
        Input example: Artist name and song title separated by a comma.
        :param line: The name of the artist and song
        :return: Lyrics of the song the user wants
        '''
        new_input = line.split(",")
        artistCreate = new_input[0]
        songCreate = new_input[1]
        lyricsFInder.findLyrics(artistCreate, songCreate)
        spotify.spot(artistCreate, songCreate)
        

    def do_open(self, line):
        """
        Given an input from the command line, open a new window with the website
        :param line: Website the user wants to open
        :return: Open a website in a new tab
        """
        openWebsite.search(line)
        first.playSound("randomxyz123.mp123") ## Can be anything you want

    def do_majokes(self, line):
        '''
        Says a joke.
        :pram line: Input to be ignored
        '''
        lame = jamesjokes.joke()
        print(lame)
        first.mainSpeech(lame, "temp.mp3")
        first.playSound("temp.mp3")
        time.sleep(8)
        first.playSound("randomxyz123.mp123") ## Can be anything you want
        
    def do_exit(self, line):
        first.mainSpeech("GoodBye! I'll see you later.", "exit.mp3")
        first.playSound("exit.mp3") ## Can be anything you want
        return True



if __name__ == '__main__':
    prompt = test()
    first.playSound("greeting.mp3")
    prompt.prompt = 'Assistant\n'
    prompt.cmdloop("Welcome Yathartha, Lets get started")
    
