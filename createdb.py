import psycopg2


class CreateDB:

    # Connection parameters for an existing database (e.g., 'postgres')
    def __init__(self, db_user, db_pass, db_to_create, host, port):
        self.master_db = 'postgres'
        self.db_user = db_user
        self.db_pass = db_pass
        self.host = host
        self.port = port
        self.db_name = db_to_create

    def create_db(self):
        conn = psycopg2.connect(database=self.master_db, user=self.db_user, password=self.db_pass, host=self.host,
                                port=self.port)
        conn.autocommit = True
        cursor = conn.cursor()
        create_db_sql = f"CREATE DATABASE {self.db_name}"
        cursor.execute(create_db_sql)

        conn.close()
        print("Database created")
