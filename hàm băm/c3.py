def polynomial_rolling_hash(s, p=31, m=10**9 + 7):
    h = 0
    for char in s:
        h = (h * p + ord(char)) % m
    return h