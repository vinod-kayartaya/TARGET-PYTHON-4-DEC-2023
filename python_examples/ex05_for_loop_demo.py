"""
Examples of a `for` loop
"""


def multiplication_table(num):
    # for index in 1, 2, 3, 4, 5, 6, 7, 8, 9, 10:
    for index in range(1, 11):
        print(f'{num} X {index} = {num * index}')


def factorial(num: int) -> int:
    if num < 2:
        return 1

    f = 1
    for n in range(num, 1, -1):
        f *= n

    return f


def main():
    n = int(input('Enter a number: '))
    line(limit=24)
    # multiplication_table(n)
    f = factorial(n)
    print(f'factorial of {n} is {f}')
    line('=', 24)


def line(char='-', limit=80):
    print(char * limit)


if __name__ == '__main__':
    main()
