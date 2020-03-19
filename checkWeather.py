import requests, json
from sys import argv

#Declaring Constants
weather_dict = {"Rain":"Rainy", "Clouds":"Cloudy", "Clear":"Sunny & Clear", "Sand":"Sand Stormy ","Drizzle":"Drizzling"}


def get_weather(KEY, location):
    openweather = ("http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}".format(location, KEY))
    r = requests.get(openweather)
    final = r.json()
    return final

def main():
    location = ""
    KEY = "Get key from openweather api "
    weather_dict = {"Rain":"Rainy", "Clouds":"Cloudy", "Clear":"Sunny & Clear", "Sand":"Sand Stormy ","Drizzle":"Drizzling"}
    for i in range(1, len(argv)):
        location += argv[i]
        location += " "
    weather = get_weather(KEY, location)
    printWeather(weather, weather_dict, location)



def printWeather(weather, weather_dict, location):
    try:
        sky = weather_dict[weather['weather'][0]['main']]
        temp = weather['main']['temp']*(9/5) - 459.67

        return ('In {} it is currently {} with a temperature of {:.2f} F'.format(location, sky, temp))
    except KeyError:
        return ("Sorry I don't have the data for {}".format(location))


if __name__ == "__main__":
    main()

