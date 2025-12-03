import time
import random

#small array for algorithms to sort
SmallArray = [3, 8, 12, 5, 19, 7, 2, 14, 9, 11]

#large array for alorithms to sort
LargeArray = [random.randint(0, 1000) for _ in range(10000)]

#bubble sort
def bubble_sort(arr):
    """Bubble sort algorithm - repeatedly swaps adjacent elements if they're in wrong order"""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

#insertion sort
def insertion_sort(arr):
    """Insertion sort algorithm - builds sorted array by inserting elements one at a time"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

#merge sort
def merge_sort(arr):
    """Merge sort algorithm - divide and conquer approach"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """Helper function to merge two sorted arrays"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

