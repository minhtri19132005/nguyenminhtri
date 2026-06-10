def count_total_passes(a):
    n = len(a)
    total_passes = 0
    
    for i in range(n - 1):
        swapped = False
        total_passes += 1  
        
        for j in range(n - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
                
        if not swapped:
            break
            
    if total_passes == 0 and n > 0:
        total_passes = 1
        
    return total_passes

mang_bai_10 = [2, 1, 3, 4]
print(f"Số lượt chạy : {count_total_passes(mang_bai_10)} lượt")
