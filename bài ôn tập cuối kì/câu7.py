def count_subarrays_with_sum(A, S):
    prefix_map = {0: 1} 
    current_sum = 0
    count = 0
    
    for num in A:
        current_sum += num
        if (current_sum - S) in prefix_map:
            count += prefix_map[current_sum - S]
        prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1
        
    return count

A = [3, 4, 7, 2, -3, 1, 4, 2]
S = 7
print(f"Số lượng mảng con thỏa mãn có tổng bằng {S} là: {count_subarrays_with_sum(A, S)}")