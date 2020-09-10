import json,requests
import click
from datetime import datetime

from src.util import get_coord, get_formated_from_timestamp, get_current_weather,get_weather_str_from_list


@click.group()
def cli():
    pass
@cli.command(name="weather")
@click.argument("city",type=str)
def weather(city):
    cor = get_coord(city)
    lat = cor[0]["coord"]["lat"]
    lon = cor[0]["coord"]["lon"]
    data = get_current_weather(lat,lon) 
    weathers = get_weather_str_from_list(data["weather"])
    timestamp_sunset = data["sys"]["sunset"]
    timestamp_sunrise = data["sys"]["sunrise"]
    temperature = data["main"]["temp"]
    print("Datetime: %s" % get_formated_from_timestamp(data["dt"]))
    print("City: %s" % data["name"])
    print("Temperature: %s" % temperature)
    print("weather: %s" % weathers)
    print("sunrise: %s" % get_formated_from_timestamp(timestamp_sunrise))
    print("sunset: %s" % get_formated_from_timestamp(timestamp_sunset))

    print("----------------------")
    print("%s, %s" % (data["name"], get_formated_from_timestamp(data["dt"])))
    print("-------------------------")
    print("%s | %s" % (temperature, weathers))

if __name__ == "__main__":
    cli()

# cor = get_coord("jakarta")
# if len(cor):
#     print(cor[0]["coord"]["lat"])
# else:
#     print('nothing')

# lat = cor[0]["coord"]["lat"]
# lon = cor[0]["coord"]["lon"]

# data = get_current_weather(lat,lon)

# weathers = get_weather_str_from_list(data["weather"])
# timestamp_sunset = data["sys"]["sunset"]
# timestamp_sunrise = data["sys"]["sunrise"]
# temperature = data["main"]["temp"]
# print("Datetime: %s" % get_formated_from_timestamp(data["dt"]))
# print("City: %s" % data["name"])
# print("Temperature: %s" % temperature)
# print("weather: %s" % weathers)
# print("sunrise: %s" % get_formated_from_timestamp(timestamp_sunrise))
# print("sunset: %s" % get_formated_from_timestamp(timestamp_sunset))

# print("----------------------")
# print("%s, %s" % (data["name"], get_formated_from_timestamp(data["dt"])))
# print("-------------------------")
# print("%s | %s" % (temperature, weathers))

