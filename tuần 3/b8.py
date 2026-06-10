def is_sorted_after_k_passes(a, k):
    n = len(a)
    # Chạy tối đa k lượt
    for i in range(min(k, n - 1)):
        for j in range(n - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                
    # Kiểm tra xem mảng đã thẳng hàng tăng dần chưa
    for i in range(n - 1):
        if a[i] > a[i+1]:
            return False
    return True

print(is_sorted_after_k_passes([3, 2, 1], k=1)) 
