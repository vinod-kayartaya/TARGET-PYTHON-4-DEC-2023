from pprint import pprint


def say_hello(name='friend', city='your city'):
    print(f'Hello {name}, how\'s weather in {city}?')


def print_sum(*args):
    # print(f'type of args is {type(args)}')
    # print(f'args is {args}')
    nums = [n for n in args if type(n) in (int, float)]
    strings = [s for s in args if type(s) is str]
    print(f'Sum of all numerical values is {sum(nums)}')
    print(f'Concatenation of all strings is {"".join(strings)}')


def create_emp(**kwargs):
    emp = dict()
    emp['name'] = kwargs.get('name')
    emp['dept'] = kwargs.get('dept', 'ADMIN')
    emp['salary'] = kwargs.get('salary', 25000)
    emp['email'] = kwargs.get('email', 'email-not-set')
    return emp


def main():
    say_hello()
    say_hello('Ramesh')
    say_hello('John', 'Dallas')
    say_hello(city='Washington')
    say_hello(city='Shivamogga', name='Ananda')

    print_sum(10, 20, 3.0, 'Vinod', 'Shyam', False, True, True, 39, 'Ramesh')
    print_sum('Shyam', 39, 22, 301)
    print_sum(301)

    e1 = create_emp(name='Ramesh', salary=50000, dept='ACCTS', manager='John')
    pprint(e1)
    e2 = create_emp(name='Rajesh')
    pprint(e2)

    d1 = {'name': 'John', 'dept': 'MARKETING'}
    e3 = create_emp(**d1)  # e3 = create_emp(name='John', dept='MARKETING')
    pprint(e3)

    vals = (10, 11, 20, 402, 39, 'asdf', 'ghjk')
    print_sum(*vals)  # print_sum(10, 11, 20, 402, 39, 'asdf', 'ghjk')
    print_sum(vals)  # print_sum((10, 11, 20, 402, 39, 'asdf', 'ghjk'))


if __name__ == '__main__':
    main()
