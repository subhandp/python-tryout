import json,requests
import click
from datetime import datetime

from src.util import get_coord, get_formated_from_timestamp, get_current_weather,get_weather_str_from_list


@click.group()
def cli():
    pass
@cli.command(name="weather")
@click.argument("city",type=str)
@click.option('--celcius', help='set celcius temperature', is_flag=True)
@click.option('--fahrenheit', help='set fahrenheit temperature',is_flag=True)
@click.option('--temp', help='Temperature Now',is_flag=True)


def weather(city,celcius,fahrenheit,temp):
    cor = get_coord(city)
    lat = cor[0]["coord"]["lat"]
    lon = cor[0]["coord"]["lon"]
    
    temp_param = "default"

    if celcius:
        temp_param = "metric"
    if fahrenheit:
        temp_param = "imperial"

    data = get_current_weather(lat,lon,temp_param) 
    
    weathers = get_weather_str_from_list(data["weather"])
    timestamp_sunset = data["sys"]["sunset"]
    timestamp_sunrise = data["sys"]["sunrise"]
    temperature = data["main"]["temp"]
    if temp_param == "metric":
        temperature = str(temperature) + " Celcius"
    elif temp_param == "imperial":
        temperature = str(temperature) + " Fahrenheit"
    else:
        temperature = str(temperature) + " Kelvin"
    
    if temp:
        print("%s, %s" % (data["name"],get_formated_from_timestamp(data["dt"])))
        print("------------------------------------------")
        print("%s | %s" % (temperature,weather))
    else:
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
