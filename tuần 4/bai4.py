def selection_sort_print_stages(a):
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        print(f" -> {a}")


print("Bài 4:")
selection_sort_print_stages([3, 1, 2])
