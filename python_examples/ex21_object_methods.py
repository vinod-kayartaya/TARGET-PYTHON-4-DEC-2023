from my_utils import dirr

class Person:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.age = kwargs.get('age')

    def __str__(self):
        name = None if self.name is None else f'"{self.name}"'
        return f'Person(name={name}, age={self.age})'

    def print(self):
        print(f"""Person details:
    Name = {self.name}
    Age  = {self.age} years\n""")

    def __setattr__(self, key, value):
        # print(f'got this attribute {key} along with a value {value}')
        if key in ('name', 'age'):  # allowed attribute list
            super().__setattr__(key, value)
        else:
            raise AttributeError('You cannot add new attributes')


if __name__ == '__main__':
    p1 = Person()
    print(dirr(p1))
    p1.name = 'Vinod Kumar'
    p1.age = 51
    # p1.email = 'vinod@vinod.co'  # the inherited (from object) __setattr__ is called here
    # p1.__setattr__('phone', '9731424784')
    print(dirr(p1))

    p2 = Person(name='Vinod', age=50)
    p3 = Person(name='Ramesh')
    p4 = Person(age=55)

    print(f'p1 is {p1}')
    print(f'p2 is {p2}')
    print(f'p3 is {p3}')
    print(f'p4 is {p4}')

    p1.print()  # python invokes the `print()` function by passing `p1` as an argument, which is received as `self`
    p2.print()
    p3.print()
    p4.print()
