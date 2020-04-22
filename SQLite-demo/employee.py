import json

class Employee:
    """A sample Employee class"""

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"


#------SQL Database Helper Functions-------#
def printEmps(func):
    def f(*args, **kwargs):
        emps, last = func(*args, **kwargs)
        if (last==None):
            print(f'{"All":<10}: {emps}')
        else:
            print(f'{last:<10}: {emps}')
        return emps, last
    return f

def insert_emp(emp, db, cursor):
    with db:
        cursor.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {
            'first': emp.first, 
            'last': emp.last, 
            'pay': emp.pay})
    get_emps(cursor, emp.last)

@printEmps
def get_emps(cursor, lastname=None):
    if lastname != None:
        cursor.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    else:
        cursor.execute("SELECT * FROM employees")
    return cursor.fetchall(), lastname

def update_pay(emp, pay, db, cursor):
    with db:
        cursor.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_emp(emp, db, cursor):
    with db:
        cursor.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

def parseEmployees(jfile):
    with open('emps.json') as f:
        data = json.load(f)

    for employee in data['employees']:
        creds = data['employees'][employee]
        emp = Employee(creds['first'], creds['last'], creds['pay'])
        yield emp