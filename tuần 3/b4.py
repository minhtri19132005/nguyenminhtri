def count_swaps(a):
    n = len(a)
    count = 0
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                count += 1
    return count

print(count_swaps([3, 2, 1])) 
