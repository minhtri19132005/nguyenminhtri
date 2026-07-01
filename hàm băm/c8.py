import math

def chi_square_test(keys, m, hash_func):
    buckets = [0] * m
    for key in keys:
        buckets[hash_func(key, m)] += 1
        
    expected = len(keys) / m
    chi_square = sum(((b - expected) ** 2) / expected for b in buckets)
    return chi_square