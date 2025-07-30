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

    def create_tables(self):
        try:
            self.cur.execute('''
            CREATE TABLE IF NOT EXISTS locations (
                id_locations SERIAL PRIMARY KEY,
                state VARCHAR(100),
                county VARCHAR(100),
                latitude DECIMAL(10,8),
                longitude DECIMAL(11,8)
            );
        ''')
            
            self.cur.execute('''
            CREATE TABLE IF NOT EXISTS climate_data (
                id_climate SERIAL PRIMARY KEY,
                location_id INT REFERENCES locations(id_locations),
                temperature DECIMAL(5,2),
                description VARCHAR(200),
                data_query TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')
            
            self.conn.commit()
            print('Tabelas criadas com sucesso!')

        except Exception as e:
            self.conn.rollback()
            print(f'Erro ao criar tabelas: {e}')

    def insert_location(self, state, country, latitude, longitude):
        query = ('''
            INSERT INTO locations (state, country, latitude, longitude)
            VALUES (%s, %s, %s, %s)
                RETURNING id_location
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
        query = '''
            SELECT state, country, temperature, description, data_query, id_location
            FROM locations
            JOIN climate_data ON locations.id_location = climate_data.location_id 
        '''
        self.cur.execute(query)
        return self.cur.fetchall()

    def delete_record(self, record_id):
        select_query = ('SELECT DISTINCT state, data_query FROM locations, climate_data')
        self.cur.execute(select_query, (record_id,))
        record_data = self.cur.fetchone()

        if record_data:
            delete_query = ('DELETE FROM climate_data WHERE id_climate = %s')
            self.cur.execute(delete_query, (record_id,))
            self.conn.commit()
            return record_data
        else:
            return None
        
    def clear_data(self):
        try:
            self.cur.execute('TRUNCATE TABLE climate_data, locations RESTART IDENTITY CASCADE')
            self.conn.commit()
        
        except Exception as e:
            self.conn.rollback()
            raise e

    def record_exists(self, record_id):
        query = ('SELECT 1 FROM climate_data WHERE id_climate = %s')
        self.cur.execute(query, (record_id,))
        return self.cur.fetchone() is not None

    def close(self):
        self.cur.close()
        self.conn.close()
