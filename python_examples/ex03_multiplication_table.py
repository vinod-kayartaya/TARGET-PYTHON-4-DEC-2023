"""
An example of using a `while` loop
"""
import math


def menu():
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
        choice = menu()

        if choice == 4:
            break

        if choice < 1 or choice > 4:
            print('Invalid choice. Please retry.')
            continue

        num = input('Enter a number: ')
        if not num.isdigit():
            print('Invalid input. Please enter a valid positive integer.')
            continue

        num = int(num)

        if choice == 1:
            print(f'Square root of {num} is {math.sqrt(num)}')
        elif choice == 2:
            print(f'Sine of {num} is {math.sin(num)}')
        elif choice == 3:
            print(f'Cosine of {num} is {math.cos(num)}')

    print('Thank you. Have a nice day.')


if __name__ == '__main__':
    main()
