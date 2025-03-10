import psycopg2

class Database:
    def __init__(self, db_name, user, password, host, port):
        self.conn = psycopg2.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cur = self.conn.cursor()

    def insert_location(self, state, country, latitude, longitude):
        query = ('''
            INSERT INTO locations (state, country, latitude, longitude)
            VALUES (%s, %s, %s, %s)
                RETURNING id
        ''')
        self.cur.execute(query, (state, country, latitude, longitude))
        locations_id = self.cur.fetchone()[0]
        self.conn.commit()
        return locations_id

    def insert_climate(self, location_id, temperature, description):
        query = ('''
            INSERT INTO climate_data (location_id, temperature, description)
            VALUES (%s, %s, %s)
        ''')
        self.cur.execute(query, (location_id, temperature, description))
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()