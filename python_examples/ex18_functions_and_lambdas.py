"""
Function arguments demo
"""
from pprint import pprint


def say_hello():
    print('Hello, world!')

def square_of(x):
    return x * x


def compare_emps(e1):
    return e1['name']


def main():
    print(say_hello)
    greet = say_hello
    print(greet)
    say_hello()
    greet()

    square = lambda x: x*x
    print(square)
    n = 12
    print(f'square of {n} is {square(n)}')

    data = [
        dict(name='Ramesh', salary=50000),
        dict(name='Rajesh', salary=78100),
        dict(name='Suresh', salary=61700),
        dict(name='Harish', salary=85000)
    ]
    # data.sort(key=compare_emps)
    # pprint(data)
    # data.sort(key=lambda e: e['salary'])
    # pprint(data)

    sorted_by_name = sorted(data, key=compare_emps)
    sorted_by_salary = sorted(data, key=lambda e: e['salary'])
    pprint(data)
    pprint(sorted_by_name)
    pprint(sorted_by_salary)

    nums = [1, 2, 3, 4, 5, 6, 9]
    sqrs = [n*n for n in nums]  # map
    evns = [n for n in nums if n % 2 == 0]  # filter
    print(nums, sqrs, evns)

    sqrs = map(lambda n: n*n, nums)
    odds = filter(lambda n: n%2, nums)
    print(nums, sqrs, odds)
    emp_names = map(lambda e: e['name'], data)

    for each_name in emp_names:
        print(each_name)


if __name__ == '__main__':
    main()
