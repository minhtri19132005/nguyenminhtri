def analyze_heap_sort_relation():
    analysis = """
    - Mối liên hệ: Cả hai thuật toán đều hoạt động theo nguyên lý chia mảng thành 2 phần (đã sắp xếp và chưa sắp xếp), liên tục tìm phần tử lớn nhất/nhỏ nhất từ phần chưa sắp xếp để đưa vào phần đã sắp xếp.
    - Điểm cải tiến: 
        + Selection sort tìm kiếm tuyến tính mất O(n) cho mỗi phần tử -> Tổng độ phức tạp O(n^2).
        + Heap sort sử dụng cấu trúc dữ liệu Max-Heap/Min-Heap giúp duy trì và lấy ra phần tử lớn nhất/nhỏ nhất chỉ mất O(log n) -> Tổng độ phức tạp cải tiến vượt bậc thành O(n log n).
    """
    return analysis.strip()

print("Bài 20:\n" + analyze_heap_sort_relation())