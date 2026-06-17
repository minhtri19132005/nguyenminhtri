def count_comparisons(a):
    n = len(a)
    comp_count = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comp_count += 1
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return comp_count


print("với n = 5:", count_comparisons([5, 4, 3, 2, 1]), "lần so sánh")
