import random

def minhash_jaccard_similarity(set_a, set_b, num_hashes=100):
    min_hash_a = []
    min_hash_b = []
    hash_seeds = [random.randint(1, 1000000) for _ in range(num_hashes)]
    
    for seed in hash_seeds:
        min_a = min(hash(item) ^ seed for item in set_a) if set_a else float('inf')
        min_b = min(hash(item) ^ seed for item in set_b) if set_b else float('inf')
        min_hash_a.append(min_a)
        min_hash_b.append(min_b)
        
    matches = sum(1 for i in range(num_hashes) if min_hash_a[i] == min_hash_b[i])
    return matches / num_hashes

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print("Ước lượng Jaccard:", minhash_jaccard_similarity(A, B)) 