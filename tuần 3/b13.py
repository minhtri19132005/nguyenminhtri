def stable_bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j][0] > a[j+1][0]:
                a[j], a[j+1] = a[j+1], a[j]
    return a
mang_b13 = [(2, 'a'), (1, 'b'), (2, 'c')]
print("Bài 13:", stable_bubble_sort(mang_b13))