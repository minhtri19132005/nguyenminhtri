def insertion_sort_multi_keys(students):
    for i in range(1, len(students)):
        key = students[i]
        j = i - 1
        while j >= 0:
            if (students[j][1] < key[1]) or (students[j][1] == key[1] and students[j][0] > key[0]):
                students[j + 1] = students[j]
                j -= 1
            else:
                break
        students[j + 1] = key
    return students

print("Bài 14:", insertion_sort_multi_keys([('An', 8), ('Ba', 9), ('Cu', 8)]))