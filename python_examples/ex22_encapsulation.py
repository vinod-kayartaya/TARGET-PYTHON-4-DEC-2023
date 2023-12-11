"""
Encapsulation - one of the 4 major OOP elements
Hides attributes
In Java/C++/C# --> achieved using private, public, protected
No such thing in Python
"""
from my_utils import dirr


class Employee:
    def __init__(self, **kwargs):
        # print('Employee.__init__() called')
        self.name = kwargs.get('name')
        self.salary = kwargs.get('salary')
        self.dept = kwargs.get('dept', 'ADMIN')

    def print(self):
        print(f"""    Name        : {self.__name}
    Salary      : {self.__salary}
    Dept        : {self.__dept}""")

    @property
    def name(self):
        return None if self.__name is None else self.__name.upper()

    @name.setter
    def name(self, value):
        if value is not None and type(value) is not str:
            raise TypeError('name must be a str')

        if value is not None:
            if len(value) < 3 or len(value) > 15:
                raise ValueError('name must be between 3 and 15 letters')

        self.__name = value

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

    @property
    def dept(self):
        return self.__dept

    @dept.setter
    def dept(self, value):
        if value is not None and type(value) is not str:
            raise TypeError('department must be str')

        self.__dept = value.upper() if type(value) is str else None


if __name__ == '__main__':
    e1 = Employee(name='John', dept='ACCT')
    print(f'type of e1.salary is {type(e1.salary)}')

    e1.print()
    e1.salary = 33000  # can trigger the setter
    e1.print()
    print(dirr(e1))

    e1.name = None
    e1.dept = 'marketing'
    e1.print()
    print(f'salary for {e1.name} is {e1.salary}')  # this is where the getter for salary is called
