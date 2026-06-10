def count_comparisons(a):
    n = len(a)
    count = 0
    for i in range(n - 1):
        for j in range(n - i - 1):
            count += 1  # Mỗi lần vào vòng lặp j là một lần so sánh
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return count

print(count_comparisons([1, 2, 3])) 