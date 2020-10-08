# TO-DO: complete the helper function below to merge 2 sorted arrays
import math


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    merged_idx = 0
    while len(arrA) > 0 and len(arrB) > 0:
        if len(arrB) > 0:

            if arrA[0] < arrB[0]:
                merged_arr[merged_idx] = arrA.pop(0)
                # arrA_idx += 1

            elif arrA[0] > arrB[0]:
                merged_arr[merged_idx] = arrB.pop(0)
        merged_idx += 1

    if len(arrA) != 0:
        while merged_idx < len(merged_arr):
            merged_arr[merged_idx] = arrA.pop(0)
            merged_idx += 1

    elif len(arrB) != 0:

        while merged_idx < len(merged_arr):

            merged_arr[merged_idx] = arrB.pop(0)
            merged_idx += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    if len(arr) > 1:
        mid = math.floor((len(arr) - 1) / 2)
        left = merge_sort(arr[:mid+1])
        right = merge_sort(arr[mid+1:])
        return merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here


arr1 = [8, 4, 5]

print(arr1[:1])
