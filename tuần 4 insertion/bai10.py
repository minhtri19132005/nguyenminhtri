def count_inversions_and_shifts(a):
   
    inversions = 0
    n = len(a)
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                inversions += 1
    return inversions


print(count_inversions_and_shifts([2, 4, 1, 3]), "nghịch thế")
