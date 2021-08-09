import os
from dotenv import load_dotenv
import json
import requests as r

load_dotenv()

WEATHER_APP_ID = os.getenv('WEATHER_KEY')

def one_call_forecast():
  response = r.get(
    'https://api.openweathermap.org/data/2.5/onecall',
    params={
      'appid': WEATHER_APP_ID,
      'lat': '51.485205',
      'lon': '0.082514',
      'exclude': 'minutely',
      'units': 'metric'
    }
  )
  return response

def write_to_file(data, filepath = 'combined_forecast.json'):
  with open(filepath, 'w+') as f:
    f.write(data)
