def count_shifts(a):
    shift_count = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            shift_count += 1  
            j -= 1
        a[j + 1] = key
    return shift_count

print( count_shifts([3, 2, 1]), "lần dịch")
