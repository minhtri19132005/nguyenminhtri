def first_uniq_char(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
        
    for i, char in enumerate(s):
        if count[char] == 1:
            return char
    return None

print(first_uniq_char('leetcode')) 