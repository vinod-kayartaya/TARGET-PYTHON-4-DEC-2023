"""
Encapsulation - one of the 4 major OOP elements
Hides attributes
In Java/C++/C# --> achieved using private, public, protected
No such thing in Python
"""
from my_utils import dirr


class Employee:
    def __init__(self, **kwargs):
        self.__name = kwargs.get('name')
        self.__salary = kwargs.get('salary')
        self.__dept = kwargs.get('dept', 'ADMIN')

    def print(self):
        print(f"""
    Name  : {self.__name}
    Salary: {self.__salary}
    Dept  : {self.__dept}\n""")

    @property  # create a setter property called 'salary'
    def salary(self):
        return self.__salary

    @salary.setter  # must have a getter first; create a writable/setter property called 'salary'
    def salary(self, value):
        if type(value) not in (int, float):
            raise TypeError('Salary must be a number')
        if value < 25000 or value > 250000:
            raise ValueError('Salary must be between 25000 and 250000')

        self.__salary = value


if __name__ == '__main__':
    e1 = Employee(name='John', dept='ACCT')
    print(f'type of e1.salary is {type(e1.salary)}')

    e1.print()
    e1.salary = 33000  # can trigger the setter
    e1.print()
    print(dirr(e1))

    print(f'e1.salary is {e1.salary}')  # this is where the getter for salary is called
