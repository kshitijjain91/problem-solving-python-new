from bs4 import BeautifulSoup
import requests
import json
import pprint

city = "London"
api_key = "228934117c8d0dffbd1cbbba41c34b4b"
api_base= "http://api.openweathermap.org/data/2.5/weather?q="
api_url = api_base + city + "&appid=" + api_key

res_weather = requests.get(api_url)
try:
    res_weather.raise_for_status()
except Exception as exc:
    print('There was an error in download {0}'.format(exc))

weather_soup = BeautifulSoup(res_weather.text, 'html.parser')
weather_dict = json.loads(str(weather_soup))
pprint.pprint(weather_dict)
print(weather_dict["name"],
    weather_dict["weather"][0]["description"],
    weather_dict["main"]["temp"],
    weather_dict['sys']['country'])