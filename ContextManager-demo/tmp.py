class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
    @fullname.setter
    def fullname(self, name):
        try:
            self.first, self.last = name.split(' ')
        except ValueError:
            print("did not work")

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first, self.last = None, None

    def __repr__(self):
        return f'Employee({self.fullname:^15})'

emp1 = Employee('John', 'Doe')
emp1.first = 'Carl'

emp1.fullname = 'James Dean'
del emp1.fullname
emp1.fullname = 'James Dean Dau'
emp1.fullname = 'James Dean'


import time
with open("tmp.txt", "w") as f:
    for _ in range(100):
        time.sleep(.01)
        print(
            "Hello world!",
            emp1,
            file=f,
            sep="\n",
        )
