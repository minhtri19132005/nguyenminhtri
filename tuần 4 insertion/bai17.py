def analyze_nearly_sorted():
    analysis = """
    - Với mảng gần như đã sắp xếp (chỉ có vài cặp sai vị trí / số nghịch thế ít), vòng lặp while phía trong của Insertion Sort sẽ dừng lại rất nhanh (thường là sau 1 hoặc vài phép so sánh).
    - Do số phép dịch chuyển (shift) cực ít, tổng số bước thực hiện trong vòng lặp con gần như là hằng số O(1).
    - Vì vậy, vòng lặp ngoài chạy n lần, đẩy tổng độ phức tạp xấp xỉ đạt mức tối ưu là O(n).
    """
    return analysis.strip()

print( analyze_nearly_sorted())