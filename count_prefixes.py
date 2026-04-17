def count_prefixes(s):
    result = {}
    n = len(s)
    for i in range(1, n + 1):
        prefix = s[:i]
        count = 0
        for j in range(n - i + 1):
            if s[j:j+i] == prefix:
                count += 1
        result[prefix] = count
    return result