# Implement the mergeSort function without using the slice operator.

def mergeSort(arr, start, end):
    if start < end:
        mid = (start + end) // 2

        mergeSort(arr, start, mid)
        mergeSort(arr, mid + 1, end)

        merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    left_len = mid - start + 1
    right_len = end - mid

    # Create temporary arrays to hold the left and right subarrays
    left_arr = [0] * left_len
    right_arr = [0] * right_len

    # Copy data from the original array to the temporary arrays
    for i in range(left_len):
        left_arr[i] = arr[start + i]
    for j in range(right_len):
        right_arr[j] = arr[mid + 1 + j]

    # Merge the left and right subarrays back into the original array
    i = 0  # Index of the left subarray
    j = 0  # Index of the right subarray
    k = start  # Index of the merged array

    while i < left_len and j < right_len:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    # Copy the remaining elements of the left subarray, if any
    while i < left_len:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    # Copy the remaining elements of the right subarray, if any
    while j < right_len:
        arr[k] = right_arr[j]
        j += 1
        k += 1

arr = [4, 2, 7, 1, 5, 3]
mergeSort(arr, 0, len(arr) - 1)
print(arr)  # Output: [1, 2, 3, 4, 5, 7]
