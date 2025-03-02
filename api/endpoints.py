from fastapi import APIRouter, HTTPException
from scripts.get_weather_data import Client

router = APIRouter()

@router.get('/weather')
def get_weather(city):
    client = Client()
    try:
        weather_data = client.get_coordinates(city=city)
        return weather_data
    except HTTPException as e:
        print(f'\nAlgo deu errado ao buscar as coordenadas: {e}')
