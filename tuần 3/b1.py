def bai_1_one_pass(a):
    n = len(a)
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
    return a

print( bai_1_one_pass([5, 1, 4, 2, 8]))