def cocktail_shaker_sort(a):
    n = len(a)
    start = 0
    end = n - 1
    swapped = True
    passes = 0 

    while swapped:
        swapped = False
        passes += 1
        
        for j in range(start, end):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
                
        if not swapped:
            break
            
        end -= 1
        swapped = False
        
        for j in range(end - 1, start - 1, -1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True

        start += 1

    return a, passes

mang_b14 = [5, 1, 4, 2, 8]
mang_sorted, so_luot = cocktail_shaker_sort(mang_b14)
print(f"Bài 14: Mảng sau xếp: {mang_sorted}, Số lượt chạy: {so_luot}")