# Weather API Client
Este é um projeto Python que consome uma API de previsão do tempo, armazena os dados em um banco de dados PostgreSQL e fornece informações sobre clima e coordenadas geográficas de cidades.

---

<br>

## Sobre o Projeto
O projeto consiste em uma aplicação que permite consultar dados meteorológicos de cidades, salvando as informações em um banco de dados para posterior análise. A aplicação utiliza APIs externas para obter coordenadas geográficas e dados climáticos.

## Tecnologias Utilizadas
 - Python 3.9
 - PostgreSQL
 - Docker
 - Bibliotecas Python:
    - requests
    - psycopg2
    - python-dotenv
    - outras (ver requirements.txt)    

## Estrutura do Projeto
```
api_Weather/
    ├── api_calls/
    │   └── weather_api.py      # Cliente principal da API
    ├── data/
    │   ├── data_coordinates.json   # Arquivo temporário para dados de coordenadas
    │   └── data_weather.json       # Arquivo temporário para dados meteorológicos
    ├── scripts/
    │   └── database.py         # Gerenciamento do banco de dados
    ├── utils/
    │   └── formatter.py        # Utilitários de formatação
    ├── Dockerfile             # Configuração do container
    ├── main.py                # Ponto de entrada da aplicação
    └── requirements.txt       # Dependências do projeto
```

## Configuração

#### Variáveis de Ambiente
É necessário criar um arquivo `.env` na raiz do projeto com as seguintes variáveis:
```
API_TOKEN=seu_token_api
COORDINATES_URL=url_api_coordenadas
WEATHER_URL=url_api_clima
DB_NAME=nome_banco
USER=usuario_banco
PASSWORD=senha_banco
HOST=host_banco
PORT=porta_banco
```
#### Banco de Dados
O projeto utiliza PostgreSQL e requer duas tabelas principais:
 - `locations`: Armazena dados de localização
 - `climate_data`: Armazena dados meteorológicos

## Docker
Para executar o projeto usando Docker:
```
docker build -t weather-api .
docker run weather-api
```

## Como Executar
1. Clone o repositório
2. Instale as dependências:
```python
pip install -r requiriments.txt
```
3. Configure as variáveis de ambiente
4. Execute a aplicação:
```python
python main.py
```

## Funcionalidades
 - Consulta de coordenadas geográficas por cidade
 - Obtenção de dados meteorológicos atuais
 - Armazenamento automático em banco de dados
 - Formatação inteligente de temperaturas

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para enviar um Pull Request.
