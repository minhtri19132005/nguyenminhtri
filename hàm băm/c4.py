def count_collisions(keys, m, hash_func):
    buckets = {}
    collisions = 0
    for key in keys:
        idx = hash_func(key, m)
        if idx in buckets:
            collisions += 1
        buckets[idx] = buckets.get(idx, 0) + 1
    return collisions