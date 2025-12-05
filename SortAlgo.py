import time
import random
import matplotlib.pyplot as plt
import numpy as np

# Generate test arrays
def generate_array(size, max_val=10000):
    return [random.randint(0, max_val) for _ in range(size)]

# Sorting Algorithms
def bubble_sort(arr):
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

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
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


# Time measurement (averaged for accuracy)
def measure_time(func, arr, runs=3):
    total = 0
    for _ in range(runs):
        copy_arr = arr.copy()
        start = time.perf_counter()
        func(copy_arr)
        total += time.perf_counter() - start
    return total / runs


# Graph plotting function
def plot_time_complexity():
    array_sizes = [10, 50, 100, 500, 1000, 5000, 10000]
    bubble_times = []
    insertion_times = []
    merge_times = []

    print("\nMeasuring algorithm performance...\n")

    for size in array_sizes:
        print(f"Testing size: {size}")
        arr = generate_array(size)

        # Only test Bubble/Insertion sort up to 2000
        if size <= 2000:
            bubble_times.append(measure_time(bubble_sort, arr))
            insertion_times.append(measure_time(insertion_sort, arr))
        else:
            bubble_times.append(None)
            insertion_times.append(None)

        merge_times.append(measure_time(merge_sort, arr))

    # Plot results
    plt.figure(figsize=(12, 7))

    plt.plot(array_sizes, merge_times, 'o-', label='Merge Sort O(n log n)')
    if any(bubble_times):
        plt.plot(array_sizes[:len(bubble_times)], bubble_times, '^-', label='Bubble Sort O(n²)')
        plt.plot(array_sizes[:len(insertion_times)], insertion_times, 's-', label='Insertion Sort O(n²)')

    plt.xlabel("Array Size (n)", fontsize=12)
    plt.ylabel("Time (seconds)", fontsize=12)
    plt.title("Sorting Algorithm Time Complexity Comparison", fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale("log")
    plt.yscale("log")

    plt.tight_layout()
    plt.show()


# Main Menu
def main():
    while True:
        print("\n" + "="*60)
        print("SORTING ALGORITHM TIME COMPLEXITY ANALYSIS")
        print("="*60)
        print("\n1. View Time Complexity Graph")
        print("2. Exit")

        choice = input("\nEnter your choice (1-2): ").strip()

        if choice == "1":
            plot_time_complexity()
        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
