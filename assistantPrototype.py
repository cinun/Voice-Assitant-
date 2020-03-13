import cmd
import weatherapi as weath
import google
from sys import argv

class test(cmd.Cmd):
    """Simple command processor example"""
    def do_printargs(self, line):
        """
        print [Arguments]
        Given a terminal print the arguments
        """
        print("Your arguments are {}".format(line))
    def do_weather(self, line):
        """
        Given a location, prints the weather
        :param line: Is the command line argument that is given to us by the user.
        :return: The current weather at a location L
        """

        temp = weath.get_weather(KEY, line)
        weath.printWeather(temp, weath.weather_dict, line)

    def do_open(self, line):
        """
        Given an input from the command line, open a new window with the website
        :param line: Website the user wants to open
        :return: Open a website in a new tab
        """
        google.search(line)
    def do_exit(self, line):
        return True



if __name__ == '__main__':
    test().cmdloop()
