from api_calls.weather_api import Client

city = 'São Paulo'

if __name__ == '__main__':
    client  = Client()
    locations_id, coordinates = client.get_coordinates(city)
    if locations_id:
        client.get_weather(locations_id, coordinates)
    client.db.close()
