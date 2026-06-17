def analyze_double_selection():
    analysis = """
    - Số vòng lặp giảm đi một nửa (n / 2 vòng).
    - Số lần so sánh tổng thể không giảm (vẫn giữ nguyên bản chất O(n^2)).
    - Trường hợp biên nguy hiểm: Khi giá trị cực đại (max) nằm ngay tại vị trí 'start', phép hoán đổi 'min' trước đó sẽ vô tình đẩy giá trị 'max' này sang vị trí 'min_idx'. Do đó, sau khi swap min, ta phải kiểm tra nếu max_idx == start thì cần cập nhật lại max_idx = min_idx rồi mới swap max về cuối.
    """
    return analysis.strip()

print("Bài 19:\n" + analyze_double_selection())