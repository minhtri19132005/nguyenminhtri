def bubble_sort_01_1(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr1 = [120, 25, 0, -42, 280, 7, 15, 10]
print("01.1 Mảng sau sắp xếp:", bubble_sort_01_1(arr1))


def bubble_sort_01_2(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

arr2 = [40, 32, 10, 12, 53, 73, 90, -1, -19, -30, -155, 75]
print("01.2 Mảng sau sắp xếp:", bubble_sort_01_2(arr2))



def bubble_sort_01_3(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

arr3 = [24, -47, 7, 44, 6, 2, 100, -2, 10, -55]
print("01.3 Mảng sau sắp xếp:", bubble_sort_01_3(arr3))


def bubble_sort_01_4(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr4 = [120, 25, 0, -42, 280, 7, 15, 10]
print("01.4 Mảng sắp xếp từ lớn đến bé:", bubble_sort_01_4(arr4))