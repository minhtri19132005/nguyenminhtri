def insert_into_sorted(a, x):
    a.append(x)
    i = len(a) - 1
    while i > 0 and a[i - 1] > x:
        a[i] = a[i - 1]
        i -= 1
    a[i] = x
    return a


print( insert_into_sorted([1, 3, 5, 7], 4))
