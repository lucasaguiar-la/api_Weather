from fastapi import FastAPI
from api.endpoints import router as api_router

app = FastAPI()
app.include_router(api_router)

@app.get('/')
def read_root():
    return {'Olá': 'Bem-vindo à Weather API!'}
