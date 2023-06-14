# Реалізувати алгоритм бінарного пошуку за допомогою рекурсії.
# Прочитати про Fibonacci search та імплементуйте його за допомогою Python.
# Визначте складність алгоритму та порівняйте його з бінарним пошуком

def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1  # Target not found

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid  # Target found
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)  # Search in the left half
    else:
        return binary_search_recursive(arr, target, mid + 1, high)  # Search in the right half

def fibonacci_search(arr, target):
    def find_fibonacci_number(limit):
        fib_prev = 0
        fib_curr = 1
        while fib_curr < limit:
            fib_prev, fib_curr = fib_curr, fib_prev + fib_curr
        return fib_prev

    n = len(arr)
    fib_m_minus_2 = find_fibonacci_number(n)
    fib_m_minus_1 = find_fibonacci_number(n + 1)

    offset = -1
    while fib_m_minus_2 > 1:
        i = min(offset + fib_m_minus_2, n - 1)
        if arr[i] < target:
            fib_m_minus_1, fib_m_minus_2 = fib_m_minus_2, fib_m_minus_1 - fib_m_minus_2
            offset = i
        elif arr[i] > target:
            fib_m_minus_1, fib_m_minus_2 = fib_m_minus_1 - fib_m_minus_2, fib_m_minus_2 - fib_m_minus_1
        else:
            return i

    if fib_m_minus_1 and offset < n - 1 and arr[offset + 1] == target:
        return offset + 1

    return -1  # Target not found

# Складність алгоритму бінарного пошуку:
#
# Найгірший випадок: O(log n), де n - кількість елементів у відсортованому масиві.
# Найкращий випадок: O(1), коли ціль знаходиться саме у середині масиву.
#
# Складність алгоритму пошуку Фібоначчі:
#
# Найгірший випадок: O(log n), де n - кількість елементів у відсортованому масиві.
# Найкращий випадок: O(1), коли ціль знаходиться саме у середині масиву.
#
# Обидва алгоритми мають подібну складність, але пошук Фібоначчі може виявитись трохи ефективнішим на практиці.