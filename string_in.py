def count_in(s, text):
    n = len(s)
    result = 0
    for i in range(n):
        shift = s[i:] + s[:i]
        for j in range(len(text)-n+1):
            if text[j:j+n] == shift:
                result+=1
    return result