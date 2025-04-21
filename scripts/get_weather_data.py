import os
import requests
import json

from dotenv import load_dotenv
from scripts.database import Database
from utils.formatter import Formatter

load_dotenv()

class Client:
    def __init__(self):
        self.api_key = os.getenv('API_KEY')
        self.coordinates_url = 'http://api.openweathermap.org/geo/1.0/direct'
        self.weather_url = 'https://api.openweathermap.org/data/2.5/weather'
        self.db = Database(
            db_name=os.getenv('DB_NAME'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            host=os.getenv('HOST'),
            port=os.getenv('PORT')
        )

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

            if not data:
                print('Nenhuma coordenada encontrada para esta cidade')
                return None

            with open('./data/coordinates_data.json', 'w') as file:
                json.dump(data, file, indent=4)

            print(f'\nLocalidade: {data[0]["state"]}')
            location_id = self.db.insert_location(
                state=data[0]['name'],
                country=data[0]['country'],
                latitude=data[0]['lat'],
                longitude=data[0]['lon']
            )

            return self.get_weather(location_id, data)

        except requests.exceptions.HTTPError as e:
            print(f'Falha na requisição de coordenadas: {e}')
            return None

    def get_weather(self, location_id, coordinates):
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
            with open('./data/weather_data.json', 'w') as file:
                json.dump(data, file)
            temperature = Formatter.format_temperature(data['main']['temp'])
            print(f'Temperatura atual: {temperature:.0f} C°\n'
                f'Descrição: {data["weather"][0]["description"].capitalize()}\n')

            self.db.insert_climate(
                location_id=location_id,
                temperature=temperature,
                description=data['weather'][0]['description']
            )

            return data
        except requests.exceptions.HTTPError as e:
            print(f'Falha ao consultar temperatura: {e}')
            return None
