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

    def insert_location(self, city, state, country, latitude, longitude):
        query = ('''
            INSERT INTO locations (city, state, country, latitude, longitude)
            VALUES (%s, %s, %s, %s, %s)
                RETURNING id
        ''')
        self.cur.execute(query, (city, state, country, latitude, longitude))
        locations_id = self.cur.fetchone()[0]
        self.conn.commit()
        return locations_id
