import psycopg2


class InsertRecord:
    def __init__(self, db_name, db_user, db_pass, host, port):
        self.db_name = db_name
        self.db_user = db_user
        self.db_pass = db_pass
        self.host = host
        self.port = int(port)

    def initialConn(self):
        conn = psycopg2.connect(database=self.db_name, user=self.db_user,
                                password=self.db_pass, host=self.host, port=self.port)
        return conn

    def insert_record(self, sql_str):
        conn = self.initialConn()
        cursor = conn.cursor()
        cursor.execute(sql_str)
        print("insert record successfully into database")
        conn.commit()
        conn.close()
