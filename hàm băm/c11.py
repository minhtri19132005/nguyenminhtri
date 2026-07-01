def hash_unordered_set(s):  
    total_hash = 0
    for item in s:
        total_hash += hash(item) 
    return total_hash

print(hash_unordered_set({1, 2, 3}) == hash_unordered_set({3, 1, 2})) 