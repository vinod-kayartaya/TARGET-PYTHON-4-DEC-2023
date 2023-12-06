"""
Examples of using lists in python.

Scalar types --> str, int, float, bool
Composite/collection --> list, tuple, dict, set

list --> [1, 2, 3]
tuple --> (1, 2, 3)

for list and tuple an element can be accessed using an index (starts from 0)

dict --> {'a': 1, 'b': 2, 'c': 3}
emp = {'name': 'john', 'dept': 'admin', 'email': 'john@xmpl.com', 'salary': 34000}

an element in a dict can be accessed using the key. eg, emp['name'] or emp['email']

set --> {1, 2, 3}  # elements cannot be accessed using an index

`len` is the common function for finding the number of elements in a list, tuple, dict, set, str
"""

each_name = 'xavior'


def main():
    # global each_name

    names = ['vinod', 'shyam', 'rohit']
    data = ['vinod', 1234, False, 1.45]

    # print(f'before loop, each_name is {each_name}')
    for each_name in names:
        print(each_name)
    print(f'after loop, each_name is {each_name}')

    print()

    for each_val in data:
        print(each_val)

    print()

    print(f'names[0] is "{names[0]}"')
    print(f'names[2] is "{names[2]}"')
    print(f'len(names) is {len(names)}')

    # print(f'names[3] is "{names[3]}"')


if __name__ == '__main__':
    main()

print(f'outside the if block, each_name is {each_name}')