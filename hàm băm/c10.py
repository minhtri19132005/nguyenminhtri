import math

def hash_multiplication(k, m, A=0.6180339887): 
    fractional_part = (k * A) % 1
    return math.floor(m * fractional_part)