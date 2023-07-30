# A bubble sort can be modified to “bubble” in both directions. The first pass moves “up” the list and the second
# pass moves “down.” This alternating pattern continues until no more passes are necessary.
# Implement this variation and describe under what circumstances it might be appropriate.

def cocktail_shaker_sort(arr):
    n = len(arr)
    start = 0
    end = n - 1
    swapped = True

    while swapped:
        swapped = False

        # Pass from left to right (up)
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        swapped = False

        # Pass from right to left (down)
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start += 1
        end -= 1


arr = [5, 2, 7, 1, 3]
cocktail_shaker_sort(arr)
print(arr)  # Output: [1, 2, 3, 5, 7]
