from threading import Thread
import time


def convert_to_uppercase(file):
    outputfile = 'temp001.txt'
    with open(outputfile, 'w') as outfile:
        for each_line in file:
            outfile.write(each_line.upper())
            time.sleep(0.25)
        # this is the last line in the context manager, and outfile is closed here
    print(f'{file.name} written in upper case to {outputfile}')


def main():
    print('Start of script execution')
    filename = 'ex29_shared_data_in_threads.py'
    file = open(filename)
    t1 = Thread(target=convert_to_uppercase, args=(file, ))
    t1.start()
    # this is the end of the `with` context-manager, and `file.close()` is called automatically
    t1.join()  # wait until t1 finishes the task and then only continue

    file.close()
    print('End of script execution')


if __name__ == '__main__':
    main()
