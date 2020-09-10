import json,requests
from datetime import datetime
import asyncio,aiohttp

from util import get_coord, get_formated_from_timestamp, get_current_weather_async


cities = ["jakarta","bandung","surabaya"]
list_task = []

async def multi_weather(cities):
    for city in cities:
        cor = get_coord(city)
        if len(cor):
            print(cor[0]["coord"]["lat"])
        else:
            print('nothing')

        lat = str(cor[0]["coord"]["lat"])
        lon = str(cor[0]["coord"]["lon"])


        task = asyncio.create_task(get_current_weather_async(lat,lon))

        # weather = await task
        # print(weather)
        list_task.append(task)

    rets = await asyncio.gather(*list_task)
    print(rets)

    # for task in list_task:
    #     weather = await task
    #     print(list(weather))



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(multi_weather(cities))

