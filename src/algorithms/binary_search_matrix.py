def binary_search(m, target):
    rows, cols = len(m), len(m[0])
    start, end = 0, rows - 1
    while start <= end:
        row = (start + end) // 2
        if target < m[row][0]:
            end = row - 1
        elif target > m[row][-1]:
            start = row + 1
        else:
            break
    if not (start <= end):
        return False

    s, e = 0, cols - 1
    row = (start + end) // 2
    while s <= e:
        mid = (s + e) // 2
        if target < m[row][mid]:
            e = mid - 1
        elif target > m[row][mid]:
            s = mid + 1
        else:
            return True
    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 7
print(binary_search(matrix, target))
