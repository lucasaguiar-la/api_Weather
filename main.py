from fastapi import FastAPI
from api.endpoints import router as api_router
from api.endpoints import Database
from dotenv import load_dotenv

import os
import uvicorn

load_dotenv()

def create_app():
    app = FastAPI()
    app.include_router(api_router)

    @app.on_event('startup')
    async def startup_event():
        db = Database(
            db_name=os.getenv('DB_NAME'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            host=os.getenv('HOST'),
            port=os.getenv('PORT')
        )
        db.create_tables()
        db.close()

    @app.get('/')
    def read_root():
        return {'Olá': 'Bem-vindo à Weather API!'}

    return app

app = create_app()

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)