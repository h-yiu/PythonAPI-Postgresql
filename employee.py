from entity import Entity


class Employee(Entity):
    id: int
    name: str
    email: str

    def __init__(self, emp_id: int = 0, name: str = '', email: str = ''):
        super().__init__('id', [emp_id, name, email])
        self.id = emp_id
        self.name = name
        self.email = email


