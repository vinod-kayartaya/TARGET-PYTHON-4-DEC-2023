"""
This is an example to check out different kinds of exceptions
"""
import sys


def main():
    # argv[0] is always the current filename
    # because, sys.argv is the list of all command line arguments passed to the `python` command
    try:
        first_input = sys.argv[1]  # '123'
        second_input = sys.argv[2]  # '4'
    except IndexError:
        print('Must supply two inputs')
        return

    try:
        num = int(first_input)  # 123
        den = int(second_input)  # 4
    except ValueError:
        print('Must supply two integers')
        return

    try:
        quot = num // den  # 30
        print(f'dividing {num} by {den} will fetch a quotient of {quot}')
    except ZeroDivisionError:
        print(f'Cannot divide {num} by 0')
        return

    print('end of main()')


if __name__ == '__main__':
    main()
    print('end of the script.')
