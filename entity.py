from create_table import CreateTable
from insert_record import InsertRecord
import configparser


def readProperties():
    config = configparser.ConfigParser()
    config.read_file(open('db.properties'))
    host = config.get('DEFAULT', 'db.host')
    port = config.get('DEFAULT', 'db.port')
    database = config.get('DEFAULT', 'db.name')
    user = config.get('DEFAULT', 'db.user')
    password = config.get('DEFAULT', 'db.password')
    return host, port, database, user, password


def mapping_type(value):
    if str(value) == "int":
        return 'INT'
    elif str(value) == "str":
        return 'TEXT'
    else:
        return None


class Entity(object):
    def __init__(self, primary_key, child_variables):
        self.primary_key = primary_key
        self.child_variables = child_variables
        self.orm_new()

    def orm_new(self):
        db_host, db_port, db_name, db_user, db_password = readProperties()
        class_name = self.__class__.__name__
        instance_variables_types = {}
        for var_name, var_type in self.__annotations__.items():
            instance_variables_types[f'{var_name}'] = f'{mapping_type(var_type.__name__)}'
        instance_variables_types['PRIMARY KEY'] = f"({self.primary_key})"
        create_table_emp = CreateTable(db_user=db_user, db_pass=db_password, columns=instance_variables_types,
                                       table_name=class_name, db_name=db_name, host=db_host, port=db_port)
        create_table_emp.create_table()
        values = ''
        for el in self.child_variables:
            values += f"'{str(el)}'" + ',' if type(el) is str else str(el) + ','
        sql_str = f"""
            INSERT INTO {class_name} VALUES ({values[:-1]});
        """
        insert_record = InsertRecord(db_user=db_user, db_pass=db_password, db_name=db_name,
                                     host=db_host, port=db_port)
        insert_record.insert_record(sql_str)

