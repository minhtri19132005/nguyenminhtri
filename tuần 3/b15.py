def sort_students(students):
    n = len(students)
    
    for i in range(n - 1):
        for j in range(n - i - 1):
            if students[j][0] > students[j+1][0]:
                students[j], students[j+1] = students[j+1], students[j]
                
    for i in range(n - 1):
        for j in range(n - i - 1):
            if students[j][1] < students[j+1][1]:
                students[j], students[j+1] = students[j+1], students[j]
                
    return students

danh_sach = [('An', 8), ('Ba', 9), ('Cu', 8)]
print("Bài 15:", sort_students(danh_sach))