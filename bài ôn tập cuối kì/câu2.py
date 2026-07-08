def insertion_sort_shifts(arr):
    A = arr.copy()
    total_shifts = 0
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            total_shifts += 1
            j -= 1
        A[j + 1] = key
    return total_shifts

A = [5, 2, 4, 6, 1, 3]
print(f"Tổng số lần dịch chuyển phần tử: {insertion_sort_shifts(A)}")