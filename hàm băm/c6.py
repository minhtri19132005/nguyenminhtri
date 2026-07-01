def rabin_karp(text, pattern, p=31, m=10**9+7):
    n, k = len(text), len(pattern)
    if k > n: return -1
    
    pattern_hash = 0
    current_hash = 0
    p_power = 1 
    
    for i in range(k):
        pattern_hash = (pattern_hash * p + ord(pattern[i])) % m
        current_hash = (current_hash * p + ord(text[i])) % m
        if i < k - 1:
            p_power = (p_power * p) % m
            
    for i in range(n - k + 1):
        if pattern_hash == current_hash and text[i:i+k] == pattern:
            return i 
        if i < n - k:
            current_hash = ((current_hash - ord(text[i]) * p_power) * p + ord(text[i+k])) % m
            current_hash = (current_hash + m) % m 
    return -1

print(rabin_karp("zabcd", "abc"))