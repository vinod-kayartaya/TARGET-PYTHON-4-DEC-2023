"""
List slice operations.

Individual element can be accessed using the subscript notation.
For example, element at index i can be accessed like nums[i].

To access a subset of the list, we can use this syntax:
nums[start: end]
* element at `end` is not included
* end = start + number_of_reqd_element

both `start` and `end` are optional
If start is omitted, then it will be considered to be `0`
If end is omitted, then it will be considered to be the len(list)

Another format:

nums[start: end: skip]
"""


def main():
    nums = [10, 12, 20, 45, 30, 91, 40, 29, 50, 78]
    nums[1] = 98
    print(nums)
    print(nums[3:8])  # elements starting from index 3 up to element at index 8-1 (or 8-3 elements)
    print(nums[0:8])  # 8 elements from index 0
    print(nums[:8])  # 8 elements from index 0
    print(nums[5:len(nums)])  # 5 elements from index 5 (i.e, len(nums) - 5)
    print(nums[5:])
    print(nums[5:-1])  # from index 5 all elements but the last one
    print(nums[:])  # all elements
    print(nums[3:8:1])  # elements at index 3, 4, 5, 6, 7
    print(nums[3:8:2])  # elements at index 3, 5, 7
    print(nums[3:8:3])  # elements at index 3, 6
    print(nums[::2])  # elements at even indices. i.e, 0, 2, 4, 6, 8
    print(nums[1::2])  # elements at odd indices. i.e, 1, 3, 5, 7, 9
    print(nums[::-1])  # elements in reverse order
    name = 'vinod kumar kayartaya'
    print(name[::-1])  # name in reverse
    nums[2:5] = [100, 200, 300]  # replaces the elements at indices 2, 3, 4 with 100, 200, 300
    print(nums)
    nums[2:5] = [1, 2, 3, 4, 5, 6]  # first 3 will replace, and the remaining will be inserted
    print(nums)
    # nums[2] = [0, 0, 0]  # this will replace the element at index 2 with a new list [0, 0, 0]
    nums[2:3] = [0, 0, 0]  # replaces the first element of the subset with 0, and other 2 0's will be inserted
    print(nums)


if __name__ == '__main__':
    main()
