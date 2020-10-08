# TO-DO: Implement a recursive implementation of binary search
import math


def binary_search(arr, target, start, end):
    # Your code here
    mid = math.floor(start + end / 2)

    if end >= start:

        if target == arr[mid]:
            print('hit here')
            return mid
        elif target < arr[mid]:
            return binary_search(arr, target, 0, mid)
        elif target > arr[mid]:
            return binary_search(arr, target, mid, len(arr))
    else:
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


# def agnostic_binary_search(arr, target):
#     # Your code here
