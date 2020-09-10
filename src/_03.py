import json,requests
from datetime import datetime
import click
from src.util import get_coord, get_formated_from_timestamp, get_current_weather_hourly,get_weather_str_from_list

@click.group()
def cli():
    pass
@cli.command(name="forecast")
@click.argument("city",type=str)
@click.option('--days', help='3 hours interval', is_flag=True)

def forecast(city,days):
    cor = get_coord(city)
    if len(cor):
        print(cor[0]["coord"]["lat"])
    else:
        print('nothing')

    lat = cor[0]["coord"]["lat"]
    lon = cor[0]["coord"]["lon"]

    data = get_current_weather_hourly(lat,lon)

    current_dt = data["current"]["dt"]
    current_day = get_formated_from_timestamp(current_dt,"%d")
    current_hour = int(get_formated_from_timestamp(current_dt,"%H"))

    hourly = data["hourly"]
    hour_interval = 3
    temp_current_hour = current_hour
    for entry in hourly:
        day = get_formated_from_timestamp(entry["dt"],"%d")
        hour = int(get_formated_from_timestamp(entry["dt"],"%H"))
        if current_day == day and hour == temp_current_hour:
            print(get_formated_from_timestamp(entry["dt"]))
            print("----------------------------------------")
            time = get_formated_from_timestamp(entry["dt"], "%H:%M:%S")
            temp = entry["temp"]
            weathers = get_weather_str_from_list(entry["weather"])
            print("%s       | %s     | %s " % (time,temp,weathers))
            temp_current_hour += hour_interval
