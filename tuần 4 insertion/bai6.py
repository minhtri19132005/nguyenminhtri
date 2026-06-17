def count_comparisons(a):
    comp_count = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            comp_count += 1  
            if a[j] > key:
                a[j + 1] = a[j]
                j -= 1
            else:
                break
        a[j + 1] = key
    return comp_count


print( count_comparisons([1, 2, 3]), "lần so sánh")
