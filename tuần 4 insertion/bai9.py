def binary_insertion_sort(a):
    comp_count = 0
    for i in range(1, len(a)):
        key = a[i]
        
        
        low = 0
        high = i - 1
        while low <= high:
            mid = (low + high) // 2
            comp_count += 1
            if key < a[mid]:
                high = mid - 1
            else:
                low = mid + 1
        
        
        for j in range(i - 1, low - 1, -1):
            a[j + 1] = a[j]
        a[low] = key
        
    return a

print( binary_insertion_sort([5, 2, 4, 6, 1, 3]))
