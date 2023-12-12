from threading import Thread
import time
import json
from ex17_csv_to_json import create_dict

class Csv2JsonTransformer(Thread):
    def __init__(self, csv_filename):
        super().__init__()
        self.__csv_filename = csv_filename

    def run(self):
        try:
            with open(self.__csv_filename, encoding='utf-8') as file:
                header = file.readline()
                data = [create_dict(header, each_line) for each_line in file]

            json_filename = f'{self.__csv_filename[:-4]}_{time.time()}.json'
            with open(json_filename, encoding='utf-8', mode='w') as file:
                json.dump(data, file, indent=4)
                print(f'{self.__csv_filename} converted to JSON and stored in {json_filename}')
        except OSError as err:
            print(f'There was an error - {err}')

def main():
    csv_filenames = ['customers.csv', 'users.csv', 'products.csv']

    print('start of script')
    for filename in csv_filenames:
        Csv2JsonTransformer(filename).start()
    print('end of script')

if __name__ == '__main__':
    main()
