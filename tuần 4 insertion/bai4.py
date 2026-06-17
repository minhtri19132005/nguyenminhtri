def insertion_sort_print_stages(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        print(f" -> {a}")


insertion_sort_print_stages([3, 1, 2])
