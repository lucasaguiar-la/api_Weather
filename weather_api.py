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

            print(f'Estado: {data[0]['state']}')

            return data
        except requests.exceptions.HTTPError as e:
            print(f'Erro: {e}')
            return None
        
    def get_weather(self, coordinates):

        coordinates_keys = [coordinates[0]['lat'], coordinates[0]['lon']]

        params = {
            'lat': coordinates_keys[0],
            'lon': coordinates_keys[1],
            'appid': self.api_key,
            'units': 'metric',
            'lang': 'pt_br'
        }

        try:
            response = requests.get(
                f'{self.base_url}weather',
                params=params
            )
            response.raise_for_status()
            data = response.json()

            temperature = data['main']['temp']
            min_temperature = data['main']['temp_min']
            max_temperature = data['main']['temp_max']
            thermal_sensation = data['main']['feels_like']
            description = data['weather'][0]['description'].capitalize()

            print(f'\nTemperatura: {temperature:.0f}ºC\n'
                f'Sensação térmica: {thermal_sensation:.0f}ºC\n'
                f'Temperatura mínima: {min_temperature:.0f}ºC\n'
                f'Temperatura máxima: {max_temperature:.0f}ºC\n'
                f'Descrição: {description}')
            return data
        except requests.exceptions.HTTPError as e:
            print(f'Erro: {e}')
            return None
