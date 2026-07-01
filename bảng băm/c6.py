"""
SO SÁNH LÝ THUYẾT:
1. Bộ nhớ: 
   - Chaining tốn thêm bộ nhớ cho con trỏ .
   - Open Addressing tiết kiệm con trỏ nhưng cần mảng kích thước đủ lớn để tránh xung đột.
2. Hiệu năng khi Hệ số tải cao:
   - Chaining suy biến tuyến tính thành O(n) chậm dần nhưng không lỗi.
   - Open Addressing giảm hiệu năng cực kỳ nhanh do hiện tượng gom cụm , dễ bị đầy.
3. Cách xóa:
   - Chaining: Xóa node trong DSLK dễ dàng.
   - Open Addressing: Không thể xóa trực tiếp vì sẽ làm đứt chuỗi dò tìm, phải dùng Lazy Deletion 
"""