import json,requests
from datetime import datetime
import click
from src.util import get_coord, get_formated_from_timestamp, get_current_weather_hourly,get_part_of_day

@click.group()
def cli():
    pass
@cli.command(name="dailyforecast")
@click.argument("city",type=str)
@click.option('--cities', help='get multi city', is_flag=True)

def dailyforecast(city,cities):
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
    current_time_day = ''
    current_day = ''
    for entry in hourly:
        day = get_formated_from_timestamp(entry["dt"],"%d")
        hour = int(get_formated_from_timestamp(entry["dt"],"%H"))
        if  get_part_of_day(hour) != current_time_day:
            if current_day != day:
                current_time_day = ''
                print("\n")
                print("----------------------------------------")
                print(get_formated_from_timestamp(entry["dt"]))
            
            time = get_formated_from_timestamp(entry["dt"], "%H:%M:%S")
            temp = entry["temp"]
        
            print("%s               | %s     " % (get_part_of_day(hour),temp))

            current_time_day = get_part_of_day(hour)
            current_day = day
