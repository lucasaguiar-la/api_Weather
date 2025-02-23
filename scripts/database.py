import psycopg2
from psycopg2 import sql
from datetime import datetime

class Database:
    def __init__(self, db_name, user, password, host, port):
        self.conn = psycopg2.connect(
            db_name=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cur = self.conn.cursor()

    
