import time
import random

#small array for algorithms to sort
SmallArray = [random.randint(0, 100) for _ in range(10)]

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

def main():
    print("="*60)
    print("SORTING ALGORITHM TIME COMPLEXITY ANALYSIS")
    print("="*60)
    
    print("\n--- SMALL ARRAY (10 elements) ---")
    small_test = SmallArray.copy()
    print(f"Array: {small_test}\n")
    
    # Bubble Sort
    start = time.time()
    result = bubble_sort(small_test.copy())
    bubble_small_time = time.time() - start
    print(f"Bubble Sort: {bubble_small_time:.6f} seconds")
    
    # Insertion Sort
    start = time.time()
    result = insertion_sort(small_test.copy())
    insertion_small_time = time.time() - start
    print(f"Insertion Sort: {insertion_small_time:.6f} seconds")
    
    # Merge Sort
    start = time.time()
    result = merge_sort(small_test.copy())
    merge_small_time = time.time() - start
    print(f"Merge Sort: {merge_small_time:.6f} seconds")
    
    print("\n--- LARGE ARRAY (10,000 elements) ---")
    
    # Bubble Sort
    start = time.time()
    result = bubble_sort(LargeArray.copy())
    bubble_large_time = time.time() - start
    print(f"Bubble Sort: {bubble_large_time:.6f} seconds")
    
    # Insertion Sort
    start = time.time()
    result = insertion_sort(LargeArray.copy())
    insertion_large_time = time.time() - start
    print(f"Insertion Sort: {insertion_large_time:.6f} seconds")
    
    # Merge Sort
    start = time.time()
    result = merge_sort(LargeArray.copy())
    merge_large_time = time.time() - start
    print(f"Merge Sort: {merge_large_time:.6f} seconds")
    
    return 0

if __name__=="__main__":
    main()