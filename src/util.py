import json,requests
from datetime import datetime

def get_coord(city:str):
    cities = "city.id.json"
    data = json.loads(open(cities).read())
    return list(filter(lambda x:x["name"].lower() == city.lower(),data))

def get_formated_from_timestamp(timestamp, format : str = None):
    date_time = datetime.fromtimestamp(timestamp)
    if format is None:
        format = "%A, %B %d, %Y %H:%M:%S"
    return date_time.strftime(format)

def get_current_weather(lat,lon):
    api_key = "1835a413e20e6815f4ebd37b86aad3cf"
    url = "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s"  % (lat, lon, api_key)
    response = requests.get(url)
    return json.loads(response.text)
