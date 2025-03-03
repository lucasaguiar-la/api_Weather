import os

from fastapi import APIRouter, HTTPException
from scripts.database import Database
from scripts.get_weather_data import Client
from dotenv import load_dotenv

load_dotenv()
router = APIRouter()

db = Database(
        db_name=os.getenv('DB_NAME'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        host=os.getenv('HOST'),
        port=os.getenv('PORT')
    )

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
    return db.get_history()

@router.delete('/delete/{record_id}')
def delete_record(record_id):
    if not db.record_exists(record_id):
        raise HTTPException(status_code=404, detail='Registro não encontrado...')
    
    db.delete_record(record_id)
    return {'message': f'Registro {record_id} excluído com sucesso!'}