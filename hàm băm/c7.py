def hash_combine(a, b):
    h_a = hash(a)
    h_b = hash(b)
    return h_a ^ (h_b + 0x9e3779b9 + (h_a << 6) + (h_a >> 2))