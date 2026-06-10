def sort_strings_by_length(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if len(a[j]) > len(a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
    return a


mang_b12 = ['abc', 'a', 'ab']
print("Bài 12:", sort_strings_by_length(mang_b12))
