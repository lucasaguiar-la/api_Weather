<<<<<<< HEAD
from weather_api import WeatherClient

if __name__ == '__main__':
    client = WeatherClient()
    coordinates = client.get_coordinates("Australia")

    if coordinates:
        data = client.get_weather(coordinates)
=======
from api_calls.weather_api import Client

city = 'São Paulo'

if __name__ == '__main__':
    client  = Client()
    data = client.get_coordinates(city)
    if data:
        client.get_weather(data)
>>>>>>> weather_branch
