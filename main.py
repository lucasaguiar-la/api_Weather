from weather_api import WeatherClient

if __name__ == '__main__':
    client = WeatherClient()
    coordinates = client.get_coordinates("São Paulo")

    if coordinates:
        data = client.get_weather(coordinates)
