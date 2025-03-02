import os

from fastapi import APIRouter, HTTPException
from scripts.database import Database
from scripts.get_weather_data import Client
from dotenv import load_dotenv

load_dotenv()
router = APIRouter()

@router.get('/weather')
def get_weather(city):
    client = Client()
    try:
        weather_data = client.get_coordinates(city=city)
        return weather_data
    except HTTPException as e:
        print(f'\nAlgo deu errado ao buscar as coordenadas: {e}')

@router.get('/history')
def get_history():
    db = Database(
        db_name=os.getenv('DB_NAME'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        host=os.getenv('HOST'),
        port=os.getenv('PORT')
    )
    history = db.get_history()
    return history
