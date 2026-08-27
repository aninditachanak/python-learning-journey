def binary_search(numbers, target, low, high):

    if low > high:
        return -1

    mid = (low + high) // 2

    if numbers[mid] == target:
        return mid

    elif target < numbers[mid]:
        return binary_search(numbers, target, low, mid - 1)

    else:
        return binary_search(numbers, target, mid + 1, high)


numbers = [10, 20, 30, 40, 50, 60, 70]

result = binary_search(numbers, 50, 0, len(numbers) - 1)

print("Index:", result)
