from api_calls.weather_api import Client

city = 'São Paulo'

if __name__ == '__main__':
    client  = Client()
    data = client.get_coordinates(city)
    if data:
        print(f'Resposta da requisição:\n{data}')