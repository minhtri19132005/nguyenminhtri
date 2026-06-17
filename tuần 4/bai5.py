def count_swaps(a):
    n = len(a)
    swap_count = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        swap_count += 1
    return swap_count


print( count_swaps([3, 2, 1]), "swap")
