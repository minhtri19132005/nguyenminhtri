def can_ship(weights, K, max_capacity):
    current_weight = 0
    trucks_needed = 1
    for w in weights:
        if current_weight + w > max_capacity:
            trucks_needed += 1
            current_weight = w
            if trucks_needed > K:
                return False
        else:
            current_weight += w
    return True

def find_min_capacity(weights, K):
    low = max(weights)
    high = sum(weights)
    ans = high
    
    while low <= high:
        mid = (low + high) // 2
        if can_ship(weights, K, mid):
            ans = mid
            high = mid - 1 
        else:
            low = mid + 1
    return ans

def distribute_packages(weights, capacity):
    distribution = []
    current_truck = []
    current_weight = 0
    for w in weights:
        if current_weight + w > capacity:
            distribution.append(current_truck)
            current_truck = [w]
            current_weight = w
        else:
            current_truck.append(w)
            current_weight += w
    if current_truck:
        distribution.append(current_truck)
    return distribution

weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
K = 5
min_cap = find_min_capacity(weights, K)
dist = distribute_packages(weights, min_cap)

print(f"Tải trọng tối thiểu tìm được: {min_cap}")
print("Cách chia kiện hàng cho 5 xe:")
for i, truck in enumerate(dist):
    print(f"  Xe {i+1}: {truck} (Tổng tải trọng: {sum(truck)})")