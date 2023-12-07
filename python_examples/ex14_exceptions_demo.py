"""
This is an example to check out different kinds of exceptions
"""
import sys


def main():
    # argv[0] is always the current filename
    # because, sys.argv is the list of all command line arguments passed to the `python` command
    num = None
    try:
        first_input = sys.argv[1]  # '123'
        second_input = sys.argv[2]  # '4'
        num = int(first_input)  # 123
        den = int(second_input)  # 4
        quot = num // den  # 30
        print(f'dividing {num} by {den} will fetch a quotient of {quot}')
    except IndexError as err:
        print(f'Must supply two inputs ({err})')
        return
    # except ValueError as err:
    #     print(f'Must supply two integers ({err})')
    #     return
    except ZeroDivisionError as err:
        print(f'Cannot divide {num} by 0 ({err})')
        return
    finally:
        print('this block (finally) executes always')
        # generally used for clean up activities

    print('end of main()')


if __name__ == '__main__':
    main()
    print('end of the script.')
