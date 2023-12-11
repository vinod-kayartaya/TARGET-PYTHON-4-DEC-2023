class Phone:
    def __init__(self):
        print('Phone.__init__() called')

    def make_call(self):
        print(f'making a call... id of self is {id(self)}')


class Radio:
    def __init__(self):
        print('Radio.__init__() called')

    def tune_to_station(self):
        print('tuning to the station...')


class MobilePhone(Phone, Radio):
    def __init__(self):
        Phone.__init__(self)
        Radio.__init__(self)
        print('MobilePhone.__init__() called')


class Camera:
    def __init__(self):
        print('Camera.__init__() called')

    def take_picture(self):
        print('taking a picture...')






class SmartPhone(MobilePhone, Camera):
    def __init__(self):
        MobilePhone.__init__(self)
        Camera.__init__(self)
        print('SmartPhone.__init__() called')


if __name__ == '__main__':
    # mp = MobilePhone()
    # mp.make_call()
    # mp.tune_to_station()
    #
    # print('-'*50)
    sp = SmartPhone()
    sp.make_call()  # SmartPhone.make_call(sp)
    print(f'id of sp is {id(sp)}')
    # sp.tune_to_station()
    # sp.take_picture()

    from pprint import pprint
    pprint(SmartPhone.mro())

    print(f'sp is an instance of SmartPhone is {isinstance(sp, SmartPhone)}')
    print(f'sp is an instance of MobilePhone is {isinstance(sp, MobilePhone)}')
    print(f'sp is an instance of Phone is {isinstance(sp, Phone)}')
    print(f'sp is an instance of Camera is {isinstance(sp, Camera)}')
    print(f'sp is an instance of Radio is {isinstance(sp, Radio)}')
    print(f'sp is an instance of object is {isinstance(sp, object)}')
    print(f'sp is an instance of int is {isinstance(sp, int)}')
    print(f'sp is an instance of str is {isinstance(sp, str)}')
