from fastapi import FastAPI
from api.endpoints import router as api_router
import uvicorn

def create_app():
    app = FastAPI()
    app.include_router(api_router)

    @app.get('/')
    def read_root():
        return {'Olá': 'Bem-vindo à Weather API!'}

    return app

app = create_app()

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)