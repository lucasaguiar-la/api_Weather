import os
import requests
from dotenv import load_dotenv

load_dotenv()

class WeatherClient:
    def __init__(self):
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        self.coordinates_url = 'http://api.openweathermap.org/geo/1.0/'
        self.base_url = 'https://api.openweathermap.org/data/2.5/'

    def get_coordinates(self, city):

        params = {
            'q': city,
            'appid': self.api_key
        }

        try:
            response = requests.get(
                f'{self.coordinates_url}direct',
                params=params
            )
            response.raise_for_status()
            data = response.json()

            print(f'Latitude: {data[0]['lat']}\n'
            f'Longitude: {data[0]['lon']}\n'
            f'Estado: {data[0]['state']}\n'
            f'País: {data[0]['country']}'
            )

            return data
        except requests.exceptions.HTTPError as e:
            print(f'Erro: {e}')
            return None
