def hash_2d_matrix(matrix, R, C, p=31, q=37, m=10**9+7):
    row_hashes = []
    for row in matrix:
        h = 0
        for i in range(C):
            h = (h * p + row[i]) % m
        row_hashes.append(h)
        
    final_hash = 0
    for j in range(R):
        final_hash = (final_hash * q + row_hashes[j]) % m
        
    return final_hash