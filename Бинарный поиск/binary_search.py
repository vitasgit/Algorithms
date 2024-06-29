def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    
    return None

lst = [1, 3, 5, 7, 9]
print(binary_search(lst, 5))  # Ожидаемый результат: 2
print(binary_search(lst, 1))  # Ожидаемый результат: 0
print(binary_search(lst, 9))  # Ожидаемый результат: 4
print(binary_search(lst, -1)) # Ожидаемый результат: None
print(binary_search(lst, 10)) # Ожидаемый результат: None
