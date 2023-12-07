def file_write_method1():
    with open('names.txt', mode='w') as file:
        count = 0
        while True:
            name = input('Enter a name (blank to stop): ')
            if name.strip() == '':
                break
            file.write(name+'\n')
            count += 1
    print(f'`names.txt` written with {count} names')


def file_write_method2():
    names = []
    while True:
        name = input('Enter a name (blank to stop): ')
        if name.strip() == '':
            break
        names.append(name)

    with open('names.txt', mode='w') as file:
        file.writelines([name+'\n' for name in names])
        print(f'`names.txt` written with {len(names)} names')


if __name__ == '__main__':
    file_write_method2()
