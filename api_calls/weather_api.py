import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

class Client:
    def __init__(self):
        self.api_key = os.getenv('API_TOKEN')
        self.coordinates_url = os.getenv('COORDINATES_URL')
        self.weather_url = os.getenv('WEATHER_URL')

    def get_coordinates(self, city):
        params = {
            'q': city,
            'appid': self.api_key
        }

        try:
            response = requests.get(
                f'{self.coordinates_url}',
                params=params
            )
            response.raise_for_status()
            data = response.json()
            with open('./data/data_coordinates.json', 'w') as file:
                json.dump(data, file)

            return data
        except requests.exceptions.HTTPError as e:
            print(f'Falha na requisição: {e}')
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
                f'{self.weather_url}',
                params=params
            )
            response.raise_for_status()
            data = response.json()
            with open('./data/data_weather.json', 'w') as file:
                json.dump(data, file)
                print('requisição bem sucedida!')
            
            return data
        except requests.exceptions.HTTPError as e:
            print(f'Falha ao consultar temperatura: {e}')
            return None