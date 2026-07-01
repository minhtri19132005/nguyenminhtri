def subarray_sum_equals_k(nums, k):
    count = 0
    prefix_sum = 0
    sum_frequencies = {0: 1} 
    
    for num in nums:
        prefix_sum += num
        if (prefix_sum - k) in sum_frequencies:
            count += sum_frequencies[prefix_sum - k]
        sum_frequencies[prefix_sum] = sum_frequencies.get(prefix_sum, 0) + 1
        
    return count

print(subarray_sum_equals_k([1, 1, 1], 2)) 