def match_found(s, text):
    n = len(s)
    m = len(text)
    pos = []
    for i in range(m-n+1):
        match = True
        for j in range(n):
            if s[j] != '?' and s[j] != text[i+j]:
                match = False
                break
        if match:
            pos.append(i)
    return pos