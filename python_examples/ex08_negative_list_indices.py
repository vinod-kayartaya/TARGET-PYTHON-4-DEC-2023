"""
List can also be accessed using a negative index
"""


def main():
    nums = [10, 12, 20, 45, 30, 91, 40, 29, 50]
    size = len(nums)
    print(f'nums is {nums}')
    print(f'size is {size}')
    print(f'first element in nums is {nums[0]}')
    print(f'first element in nums is {nums[-size]}')

    print(f'the last element in nums is {nums[size-1]}')
    print(f'the last element in nums is {nums[-1]}')

    print(f'the 3rd last in nums is {nums[-3]}')
    nums.insert(-999, 123)  # inserts at the index 0, assuming that -999 is not a valid index
    print(f'nums is {nums}')


if __name__ == '__main__':
    main()
