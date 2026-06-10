def element_after_one_pass(a):
    n = len(a)
    if n == 0: return None
    for j in range(n - 1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
    return a[n-1]
print(element_after_one_pass([4, 2, 7, 1, 3])) 
