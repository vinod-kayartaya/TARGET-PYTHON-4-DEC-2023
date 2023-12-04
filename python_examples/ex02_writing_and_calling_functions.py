"""
This is an example for understanding functions.

A function in Python is created using the `def` keyword. It is important to indent the
code properly.
"""


def check_if_num_is_even_or_odd():
    """
    This is a function to accept a number from the user and check if it is even or odd.
    If the user enters a non-numerical value, this function gives an error message.
    """
    num = input('Enter a number: ')

    if num.isdigit():
        num = int(num)
        if num % 2 == 0:
            print(f'{num} is an even number.')
        else:
            print(f'{num} is an odd number')
    else:
        print('Invalid value given. Must give int.')


if __name__ == '__main__':
    check_if_num_is_even_or_odd()

# print('the name of this module is', __name__)
# __name__ is a builtin variable for every module. The value of this variable
# changes based on what are you doing with this module.
# 1. Are you executing this module?
#    - the name is '__main__'
# 2. Are you importing this module?
#    - the name is same as the filename (base name)
