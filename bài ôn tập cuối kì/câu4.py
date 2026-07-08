def daily_temperatures(T):
    ans = [0] * len(T)
    stack = []  
    
    for i in range(len(T)):
        while stack and T[i] > T[stack[-1]]:
            prev_index = stack.pop()
            ans[prev_index] = i - prev_index
        stack.append(i)
        
    return ans

T = [73, 74, 75, 71, 69, 72, 76, 73]
print(f" {daily_temperatures(T)}")