# One way to improve the quicksort is to use an insertion sort on lists that are small in length
# (call it the “partition limit”). Why does this make sense? Re-implement the quicksort and use it to sort a random
# list of integers. Perform analysis using different list sizes for the partition limit.

import random
import timeit

def quicksort(arr, partition_limit=10):
    if len(arr) <= partition_limit:
        insertion_sort(arr)
    else:
        _quicksort(arr, 0, len(arr) - 1)


def _quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        _quicksort(arr, low, pivot_index - 1)
        _quicksort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

list_sizes = [100, 1000, 10000]  # Different list sizes to test
partition_limits = [5, 10, 20]  # Different partition limits to test

for size in list_sizes:
    for limit in partition_limits:
        arr = random.sample(range(size), size)
        time = timeit.timeit(lambda: quicksort(arr, limit), number=1)
        print(f"List size: {size}, Partition limit: {limit}, Execution time: {time:.6f} seconds")