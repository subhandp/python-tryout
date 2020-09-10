import json,requests
from datetime import datetime

from util import get_coord, get_formated_from_timestamp, get_current_weather

cor = get_coord("jakarta")
if len(cor):
    print(cor[0]["coord"]["lat"])
else:
    print('nothing')

# api_key = "1835a413e20e6815f4ebd37b86aad3cf"
lat = cor[0]["coord"]["lat"]
lon = cor[0]["coord"]["lon"]
# url = "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s"  % (lat, lon, api_key)
# response = requests.get(url)
# data = json.loads(response.text)
data = get_current_weather(lat,lon)
weathers = ','.join(
    list(map(lambda x: x['main'], data["weather"]))
    )
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

