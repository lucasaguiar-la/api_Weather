import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class WeatherClient:
    def __init__(self):
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        self.base_url = 'https://api.openweathermap.org/data/2.5/'

    def get_historical_weather(self, city, date):
        timestamp = int(datetime.strptime(date, '%y-"m-"d').timestamp())

        params = {
            'q': city,
            'dt': timestamp,
            'appid': self.api_key,
            'units': 'metric',
            'lang': 'pt_br'
        }
