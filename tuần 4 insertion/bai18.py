def analyze_search_direction():
    analysis = """
    - Dò từ phải sang trái (Chuẩn): Phù hợp tuyệt đối với dữ liệu thực tế hoặc dữ liệu gần như đã sắp xếp. Do mảng bên trái đã tăng dần, phần tử mới thường lớn hơn các phần tử cuối đoạn đã xếp nên vòng lặp dừng ngay lập tức -> Rất hiệu quả.
    - Dò từ trái sang phải: Phải duyệt qua tất cả các phần tử nhỏ hơn từ đầu mảng để tìm vị trí chèn, tốn nhiều phép so sánh hơn đối với dữ liệu đã gần đúng vị trí ở cuối.
    """
    return analysis.strip()

print(analyze_search_direction())