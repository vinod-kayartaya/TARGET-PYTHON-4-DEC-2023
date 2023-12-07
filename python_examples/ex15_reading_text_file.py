"""
Different ways to read a text file
"""
FILENAME = '/Users/vinod/Desktop/react-redux-toolkit-addressbook-app/src/App.js'


def file_read_method1():
    file = None
    try:
        file = open(FILENAME)
        while True:
            line = file.readline()
            if line == '':
                break
            print(line, end='')
    except OSError as err:
        print(f'There was an error - {err}')
    finally:
        if file is not None:
            file.close()


def file_read_method2():
    try:
        with open(FILENAME) as file:
            all_lines = file.readlines()
            for each_line in all_lines:
                print(each_line, end='')
            # last thing to be executed here is `file.close()`
    except OSError as err:
        print(f'There was an error - {err}')


def file_read_method3():
    try:
        with open(FILENAME) as file:
            for each_line in file:
                print(each_line, end='')
            # last thing to be executed here is `file.close()`
    except OSError as err:
        print(f'There was an error - {err}')


def file_read_method4():
    try:
        with open(FILENAME) as file:
            file_content = file.read()
            # last thing to be executed here is `file.close()`
        print(file_content)
    except OSError as err:
        print(f'There was an error - {err}')


if __name__ == '__main__':
    file_read_method4()
