def count_exact_swaps(a):
    n = len(a)
    exact_swap_count = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            exact_swap_count += 1
    return exact_swap_count


print( count_exact_swaps([1, 2, 3]), "swap")
