from createdb import CreateDB
from employee import Employee


def create_db():
    creating = CreateDB(db_user="postgres", db_pass="your-password",
                        db_to_create="pythonAPIdb", host="localhost", port="5432")
    creating.create_db()


if __name__ == '__main__':
    employee = Employee(emp_id=1, name="John", email='john@h-yao.io')
