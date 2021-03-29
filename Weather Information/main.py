import requests
from pprint import pprint

API_key = '159eff4205872b0f876ea8973863dd9a' # https://home.openweathermap.org/api_keys

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/forecast?appid=" + API_key + "&q=" + city

weather_data = requests.get(base_url).json()

pprint(weather_data)
