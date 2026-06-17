def analyze_swaps_comparison():
    analysis = """
    - Selection Sort: Luôn dùng tối đa (n - 1) lần swap vì mỗi vòng chọn chỉ hoán đổi 1 lần duy nhất.
    - Bubble Sort: Số lần swap bằng chính xác số cặp nghịch thế (inversions). Trong trường hợp xấu nhất (mảng ngược), số swap là n*(n-1)/2.
    -> Giải thích chênh lệch: Selection sort tìm phần tử tối ưu trước rồi mới swap một lần về vị trí đúng, còn Bubble sort hoán đổi liên tục các phần tử kề nhau trên đường đi nên tốn nhiều swap hơn.
    """
    return analysis.strip()

print("Bài 18:\n" + analyze_swaps_comparison())