def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + equal + quicksort(right)


array = [5, 2, 8, 12, 1]
sorted_array = quicksort(array)
print(sorted_array)
