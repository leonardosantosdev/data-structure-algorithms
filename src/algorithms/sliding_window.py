def max_profit(lst):
    left = 0
    right = 1
    max_profit = 0
    while right < len(lst):
        if lst[right] > lst[left]:
            profit = lst[right] - lst[left]
            max_profit = max(max_profit, profit)
        else:
            left = right
        right += 1

    return max_profit


lst = [1, 4, 3, 2, 6, 5, 1, 2,]
print(max_profit(lst))
