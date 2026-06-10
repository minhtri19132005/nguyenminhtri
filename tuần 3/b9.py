def bubble_sort_early_exit(a):
    n = len(a)
    passes = 0
    
    for i in range(n - 1):
        swapped = False
        passes += 1 
        
        for j in range(n - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True  
        if not swapped:
            break
            
    if passes == 0 and n > 0:
        passes = 1
        
    return passes

mang_bai_9 = [1, 2, 3, 4]
print(f"Số lượt chạy: {bubble_sort_early_exit(mang_bai_9)} lượt")
