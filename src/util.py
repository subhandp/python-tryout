import json,requests
import asyncio,aiohttp
from datetime import datetime

api_key = "1835a413e20e6815f4ebd37b86aad3cf"

def get_part_of_day(hour):
    return (
        "morning" if 5 <= hour <= 11
        else
        "afternoon" if 12 <= hour <= 17
        else
        "evening" if 18 <= hour <= 22
        else
        "night"
    )

def get_weather_str_from_list(list_weather):
    return ','.join(
    list(map(lambda x: x['main'], list_weather))
    )

def get_coord(city:str):
    cities = "src/city.id.json"
    data = json.loads(open(cities).read())
    return list(filter(lambda x:x["name"].lower() == city.lower(),data))


def get_formated_from_timestamp(timestamp, format : str = None):
    date_time = datetime.fromtimestamp(timestamp)
    if format is None:
        format = "%A, %B %d, %Y %H:%M:%S"
    return date_time.strftime(format)

def get_current_weather(lat,lon):
    url = "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s"  % (lat, lon, api_key)
    response = requests.get(url)
    return json.loads(response.text)

def get_current_weather_hourly(lat,lon):
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s"  % (lat, lon, api_key)
    response = requests.get(url)
    return json.loads(response.text)
    
async def fetch_async(session, url,params={}):
    async with session.get(url,params=params) as response:
        return await response.json()

async def get_current_weather_async(lat,lon):
    params = {"lat": lat,"lon": lon,"appid": api_key}
    url = "https://api.openweathermap.org/data/2.5/weather"
    async with aiohttp.ClientSession() as session:
        async with session.get(url,params=params) as response:
            # print(response.)
            return response.json()


