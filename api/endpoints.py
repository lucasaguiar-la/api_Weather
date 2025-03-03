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
def get_weather(city: str):
    client = Client()
    try:
        weather_data = client.get_coordinates(city=city)
        if not weather_data:
            raise HTTPException(status_code=404, detail='Dados meteorológicos não encontrados...')

        temperature =  weather_data['main']['temp']
        description = weather_data['weather'][0]['description'].capitalize()

        return {
            'Cidade': city,
            'Temperatura': f'{temperature:.0f} ºC',
            'Descrição': description
                }

    except HTTPException as e:
        print(f'\nAlgo deu errado ao buscar as coordenadas: {e}')
        return e

@router.get('/history')
def get_history():
    return db.get_history()

@router.delete('/delete/{record_id}')
def delete_record(record_id: int):
    try:
        result = db.delete_record(record_id)
        if not result:
            raise HTTPException(status_code=404, detail='Registro não encontrado...')

        city_record = result[0]
        data_record = str(result[1])

        return {
            'Sucesso': f'Registro {record_id} excluído com êxito!',
            'Cidade': f'{city_record}',
            'Data da consulta': f'{data_record.split(' ')[0]}'
            }

    except HTTPException as e:
        print(f'\nAlgo deu errado ao tentar deletar o registro: {e}')
        return e

@router.delete('/all')
def delete_all_records():
    try:
        db.clear_data()
        return {
            'Sucesso': 'Todos os dados foram apagados com êxito!'
        }
    except HTTPException as e:
        print(f'\nAlgo deu errado ao tentar deletar o registro: {e}')
        return e
