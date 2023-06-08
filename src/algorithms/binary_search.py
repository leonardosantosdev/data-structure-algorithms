def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


array = [1, 2, 5, 8, 12, 15, 18]
target = 1
result = binary_search(array, target)
if result != -1:
    print(f"The element {target} wasnt found in index {result}.")
else:
    print(f"The element {target} wasnt found in the list.")
