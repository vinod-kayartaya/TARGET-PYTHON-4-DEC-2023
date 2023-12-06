"""
An example of using a `while` loop
"""
import math


def menu() -> int:
    """
    Displays a menu for the user, accepts the choice from the user, and
    returns the integer version of the value entered by the user. If the user
    inputs a non-numeric value, then -1 is returned.

    :return: int version of the input for numerical inputs, -1 for non-numerical inputs
    """
    print("""Main menu:
    1. Square root
    2. Sine
    3. Cosine
    4. Exit""")
    choice = input('Enter your choice: ')
    if not choice.isdigit():
        return -1

    return int(choice)


def main():
    while True:
        answer = menu()

        if answer == 4:
            break

        if answer < 1 or answer > 4:
            print('Invalid choice. Please retry.')
            continue

        num = input('Enter a number: ')
        if not num.isdigit():
            print('Invalid input. Please enter a valid positive integer.')
            continue

        num = int(num)

        if answer == 1:
            print(f'Square root of {num} is {math.sqrt(num)}')
        elif answer == 2:
            print(f'Sine of {num} is {math.sin(num)}')
        elif answer == 3:
            print(f'Cosine of {num} is {math.cos(num)}')

    print('Thank you. Have a nice day.')


if __name__ == '__main__':
    main()
