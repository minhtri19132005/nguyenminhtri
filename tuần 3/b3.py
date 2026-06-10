def bubble_sort_descending(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] < a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

print(bubble_sort_descending([5, 1, 4, 2, 8])) 
