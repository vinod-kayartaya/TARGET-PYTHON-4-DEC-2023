class Test:
    some_data = [100, 'vinod']  # static (global) data 

    def __init__(self):
        self.more_data = []  # non-static (object) member data

    @staticmethod  # cannot use the non-static / object member data
    def say_hello(name, city):
        print(f'Hello {name}! how\'s weather in {city}?')

    @classmethod  # cannot use the non-static / object member data
    def greet(cls, name, city):
        print(f'cls is {cls}')  # Java: this.getClass()
        print(f'Hello {name}! how\'s weather in {city}?')


if __name__ == '__main__':
    Test.say_hello('Vinod', 'Bangalore')
    Test.greet('Vinod', 'Bangalore')
    t1 = Test()
    t1.say_hello('Shyam', 'Shivamogga')
    t1.greet('Shyam', 'Shivamogga')
    t2 = Test()
    print(f't1.some_data is {t1.some_data}')
    print(f't2.some_data is {t2.some_data}')
    print(f't1.more_data is {t1.more_data}')
    print(f't2.more_data is {t2.more_data}')
    t2.some_data.extend([200, 'kumar'])
    t2.more_data.extend([300, 'bangalore'])
    print(f't1.some_data is {t1.some_data}')
    print(f't2.some_data is {t2.some_data}')
    print(f't1.more_data is {t1.more_data}')
    print(f't2.more_data is {t2.more_data}')

