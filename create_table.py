import psycopg2


class CreateTable:
    def __init__(self, db_name, db_user, db_pass, host, port, table_name, columns):
        self.db_name = db_name
        self.db_user = db_user
        self.db_pass = db_pass
        self.host = host
        self.port = port
        self.table_name = table_name
        self.columns = columns

    def build_columns_string(self):
        str_columns = ""
        for key, value in self.columns.items():
            str_columns += key + " " + str(value) + ",\n\t"
        return str_columns[:-3]

    def buildString(self):
        str_columns = self.build_columns_string()
        sql = f"""
        DROP TABLE IF EXISTS {self.table_name} CASCADE;
        CREATE TABLE {self.table_name} (
            {str_columns}
        );
        """
        return sql

    def initialConn(self):
        conn = psycopg2.connect(database=self.db_name, user=self.db_user,
                                password=self.db_pass, host=self.host, port=self.port)
        return conn

    def create_table(self):
        conn = self.initialConn()
        cursor = conn.cursor()
        cursor.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables "
                       f"WHERE table_name = '{self.table_name.lower()}')")
        # print(cursor.fetchone()[0])
        if cursor.fetchone()[0]:
            print("Table already exists")
            cursor.close()
        else:
            sql = self.buildString()
            cursor.execute(sql)
            conn.commit()
            conn.close()
            print(f"Table {self.table_name} created successfully")
