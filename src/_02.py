import json,requests
from datetime import datetime
import asyncio,aiohttp
import click

from src.util import get_coord, get_formated_from_timestamp, get_current_weather_async


@click.group()
def cli():
    pass
@cli.command(name="weathers")
@click.option('--cities', is_flag=True, help='Temperature multi city')
@click.argument("city",type=str, nargs=-1)

def weathers(cities,city):
    cities_param = city
    list_task = []
    async def multi_weather(cities_param):
        for city in cities_param:
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
        loop.run_until_complete(weathers(cities,city))

