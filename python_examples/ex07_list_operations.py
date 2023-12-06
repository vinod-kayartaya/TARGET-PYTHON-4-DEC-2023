"""
List methods and operations

Methods in the `list` class:
'append', 'insert', 'clear', 'index', 'pop', 'remove', 'count', 'reverse', 'sort', 'extend', 'copy'
"""


def main():
    nums = [10, 20, 30]
    print(nums)
    nums.append(40)
    print(nums)
    nums.insert(0, 50)  # nums.insert(0, 50)
    print(nums)
    nums.insert(500, 60)  # no error even if the index 500 is out of boundary; appends to the end.
    print(nums)
    nums.clear()  # empties the list
    print(nums)
    nums = [50, 10, 20, 30, 40, 60, 30, 12, 30, 22]
    n = 40
    if n in nums:
        i = nums.index(n)
        print(f'{n} is found at index {i} in the list {nums}')
    else:
        print(f'{n} does not exist in the list {nums}')

    n = nums.pop()  # removes the last element
    print(f'after popping {n} the list is {nums}')
    n = nums.pop(1)  # removes the element at index 1
    print(f'after popping {n} the list is {nums}')
    x = 20
    if x in nums:
        nums.remove(x)  # removes if 20 exists in nums; else raises ValueError
        print(f'after removing {x} the list is {nums}')
    else:
        print(f'cannot remove {x}, since it is not in the list')

    x = 30
    c = nums.count(x)
    print(f'{x} appears {c} times in {nums}')

    print(nums)
    nums.reverse()
    print('after reversing nums is', nums)
    nums.sort()
    print('after sorting nums is', nums)
    nums.sort(reverse=True)
    print('after sorting in reverse order, nums is', nums)

    even_nums = [2, 4, 6, 8]
    nums.append(even_nums)
    print(f'after appending {even_nums} to nums, it is {nums}')
    nums.pop()  # removes the last element
    nums.extend(even_nums)
    print(f'after extending {even_nums} to nums, it is {nums}')
    odd_nums = [1, 3, 5]
    nums += odd_nums
    print(f'after nums += odd_nums, nums is {nums}')

    names = ['vinod', 'shyam']
    print(names)
    # names += 'kiran'  # str is equivalent of a list of letters.
    names += ['kiran']
    print(names)


if __name__ == '__main__':
    main()
