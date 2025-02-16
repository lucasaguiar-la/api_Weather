import os
import requests
from dotenv import load_dotenv

load_dotenv()

class Client:
    def __init__(self):
        self.api_key = os.getenv('API_TOKEN')
        self.coordinates_url = os.getenv('COORDINATES_URL')

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
            print('Requisição bem sucedida!')
            return data
        except requests.exceptions.HTTPError as e:
            print(f'Falha na requisição: {e}')
            return None