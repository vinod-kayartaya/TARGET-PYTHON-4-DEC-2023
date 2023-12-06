"""
A dict is a collection type where each value is given a key.
"""
from pprint import pprint
from my_utils import dirr


def main():
    p1 = dict(name='Vinod Kumar', age=50, married=True, gender='Male', phone_numbers=['9731424784'])
    pprint(p1)
    p2 = {'fname': 'Shyam', 'city': 'Bangalore'}
    pprint(p2)
    pprint(dirr(dict))
    print(f'name of p1 is {p1["name"]}')
    print(f'email of p1 is {p1.get("email", "unknown")}')
    print(f'phone numbers of p1 is {p1.get("phone_numbers", "unknown")}')
    print(f'list of all keys in p1 --> {p1.keys()}')
    print(f'list of all values in p1 --> {p1.values()}')

    for each_item in p1.items():
        print(f'{each_item[0]} --> {each_item[1]}')

    popped_value = p1.pop('married')
    print(f'popped_value is {popped_value}')
    pprint(p1)

    popped_value = p1.pop('email', None)
    print(f'popped_value is {popped_value}')
    pprint(p1)

    p1['email'] = 'vinod@vinod.co'  # adds a new entry
    p1['email'] = 'vinod@knowledgeworksindia.com'  # replaces the old one
    p1['email'] = 'kayartaya.vinod@gmail.com'  # replaces the old one
    pprint(p1)

    keys = ['fname', 'lname', 'city', 'email', 'phone', 'gender']
    p3 = dict.fromkeys(keys)
    pprint(p3)
    p3.update({'fname': 'Ravi', 'city': 'Chennai'})
    pprint(p3)
    p3.update(p2)
    pprint(p3)
    update_info = [('gender', 'Male'), ('email', 'ravi@xmpl.com'), ('country', 'India')]
    p3.update(update_info)
    pprint(p3)


if __name__ == '__main__':
    main()
