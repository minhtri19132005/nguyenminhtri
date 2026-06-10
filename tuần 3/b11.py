def sort_by_absolute_value(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if abs(a[j]) > abs(a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
    return a

mang_b11 = [-3, 1, -2, 2]
print("Bài 11:", sort_by_absolute_value(mang_b11))
