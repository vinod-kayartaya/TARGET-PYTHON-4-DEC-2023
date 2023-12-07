import time
import json


def create_dict(header: str, value: str) -> dict:
    """
    This method is supposed to receive two strings consisting of headers and matching values and return a dict
    consisting of keys from header and values from values
    :param header: comma separated keys in a str
    :param value: comma separated values in a str
    :return: dict with keys and values from the parameters
    """
    keys = header.rstrip().split(',')
    values = value.rstrip().split(',')
    return dict(zip(keys, values))


def csv2json(filename: str) -> None:
    try:
        with open(filename, encoding='utf-8') as file:
            header = file.readline()
            data = [create_dict(header, each_line) for each_line in file]
            print(f'data contains {len(data)} elements')

        new_filename = f'{filename[:-4]}_{time.time()}.json'
        with open(new_filename, encoding='utf-8', mode='w') as file:
            json.dump(data, file, indent=4)
            print(f'{filename} converted to JSON and stored in {new_filename}')
    except OSError as err:
        print(f'There was an error - {err}')


if __name__ == '__main__':
    csv2json('customers.csv')
