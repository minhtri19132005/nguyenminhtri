def hash_string_sum(s, m):

    total = sum(ord(char) for char in s)
    return total % m

print(hash_string_sum('abc', 100) == hash_string_sum('cba', 100))  