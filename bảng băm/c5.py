def group_by_first_char(words):
    groups = {}
    for word in words:
        key = word[0] if word else ""
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return groups

print(group_by_first_char(["apple", "banana", "apricot", "berry"]))