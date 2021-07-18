from urllib.request import urlopen
import requests
import json
from .models import Profile
import logging

logger = logging.getLogger(__name__)

def get_location():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    return json.load(response)['city']

def weather(city):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=bcd280d6f83f1d32efee8a980ceaccc9"
    data = requests.get(url.format(city)).json()
    if 'main' in data:
        city_weather = {
            'temp': data['main']['temp'],
            'desc': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
    else:
        city_weather = {
            'temp': '--',
            'desc': 'The weather is not available for this city, Please change to a nearby popular location',
            'icon': '04d'
        }
    return city_weather

def update_location_weather(location):
    new_weather = weather(location.city)
    location.temp = new_weather['temp']
    location.desc = new_weather['desc']
    location.icon = new_weather['icon']
    location.save()

def stale_location(loc_object):
    if not Profile.objects.filter(location=loc_object):
        logger.info(loc_object.city + ' has been deleted from DB')
        loc_object.delete()