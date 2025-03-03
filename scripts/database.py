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

    def get_history(self):
        query = ('SELECT * FROM climate_data')
        self.cur.execute(query)
        return self.cur.fetchall()
    
    def record_exists(self, record_id):
        query = ('SELECT 1 FROM climate_data WHERE id = %s')
        self.cur.execute(query, (record_id,))
        return self.cur.fetchone() is not None
    
    def delete_record(self, record_id):
        query = ('DELETE FROM climate_data WHERE id = %s')
        self.cur.execute(query, (record_id,))
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()