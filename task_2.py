from random import randint


def partition(arr, left, right, pivotIndex):
    pivotValue = arr[pivotIndex]
    arr[pivotIndex], arr[right] = arr[right], arr[pivotIndex]
    storeIndex = left
    for i in range(left, right):
        if arr[i] < pivotValue:
            arr[storeIndex], arr[i] = arr[i], arr[storeIndex]
            storeIndex += 1
    arr[right], arr[storeIndex] = arr[storeIndex], arr[right]
    return storeIndex


def select(arr, left, right, k):
    if left == right:
        return arr[left]
    pivotIndex = randint(left, right)
    pivotIndex = partition(arr, left, right, pivotIndex)
    if k == pivotIndex:
        return arr[k]
    elif k < pivotIndex:
        return select(arr, left, pivotIndex - 1, k)
    else:
        return select(arr, pivotIndex + 1, right, k)


# Приклад використання
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_value = select(arr, 0, len(arr) - 1, 3)
print(sorted_value)  # [3, 9, 10, 27, 38, 43, 82]
