"""
List comprehension - create a new list from a given list without iteration
"""
import math
from my_utils import dirr


def is_odd(n):
    return n % 2 == 1


def main():
    nums = [10, 12, 13, 45, 30, 91, 40, 29, 50, 78]
    even_nums = []
    for each_num in nums:
        if each_num % 2 == 0:
            even_nums.append(each_num)
    print(f'even_nums is {even_nums}')

    # filter operation
    # [append_value for each_elem in list_elems if condition]
    odd_nums = [n for n in nums if is_odd(n)]  # 0 --> False, Non-zero --> True
    print(f'odd_nums is {odd_nums}')

    # map operations
    squares = [n*n for n in nums]
    square_roots = [math.sqrt(n) for n in nums if n % 2 == 0]
    print(f'squares is {squares}')
    print(f'square_root is {square_roots}')

    print(f'attributes of str are: {dirr(str)}')


if __name__ == '__main__':
    main()
