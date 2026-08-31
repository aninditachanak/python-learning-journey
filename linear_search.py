def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


numbers = [10, 25, 30, 45, 50, 65, 70]

target = int(input("Enter the number to search: "))

result = linear_search(numbers, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
