import requests, json
from sys import argv


weather_dict = {"Rain":"Rainy", "Clouds":"Cloudy", "Clear":"Sunny & Clear", "Sand":"Sand Stormy ","Drizzle":"Drizzling"}

def get_weather(KEY, location):
    openweather = ("http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}".format(location, KEY))
    r = requests.get(openweather)
    final = r.json()
    return final

def main():
    location = ""
    KEY = "e0b1a3f7e2a349c5da6ae97ed5cdbd74"
    weather_dict = {"Rain":"Rainy", "Clouds":"Cloudy", "Clear":"Sunny & Clear", "Sand":"Sand Stormy ","Drizzle":"Drizzling"}
    for i in range(1, len(argv)):
        location += argv[i]
        location += " "
    weather = get_weather(KEY, location)
    printWeather(weather, weather_dict, location)



def printWeather(weather, weather_dict, location):
    try:
        sky = weather_dict[weather['weather'][0]['main']]
        temp = weather['main']['temp']
        print("In {} it is currently {} with a temperature of {} F".format(location, sky, temp))
    except KeyError:
        print("Sorry I don't have the data for {}".format(location))


if __name__ == "__main__":
    main()

