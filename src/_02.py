import json,requests
from datetime import datetime

from util import get_coord, get_formated_from_timestamp

cities = ["jakarta","bandung","surabaya"]

for city in cities:
    k = get_coord(city)
    print(k)