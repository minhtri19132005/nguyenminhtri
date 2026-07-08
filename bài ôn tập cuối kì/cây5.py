from collections import deque

def max_sliding_window_min(A, k):
    dq = deque()
    res = []
    
    for i in range(len(A)):
        if dq and dq[0] < i - k + 1:
            dq.popleft()
            
        while dq and A[dq[-1]] >= A[i]:
            dq.pop()
            
        dq.append(i)
        
        if i < 3:
            print(f"Bước {i+1} (i={i}, phần tử={A[i]}): Deque chứa chỉ số {list(dq)} (giá trị tương ứng {[A[x] for x in dq]})")
            
        if i >= k - 1:
            res.append(A[dq[0]])
            
    return res

A = [4, 2, 12, 11, -5, 8, 1, 5, 6]
k = 3
print("-" * 40)
result = max_sliding_window_min(A, k)
print(f" {result}")