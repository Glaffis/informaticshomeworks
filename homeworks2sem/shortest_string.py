def shortest_string(s):
    if not s:
        return ''
    words = list(s)
    while len(words)>1:
        i_1, m_1, j_1= 0, 0, 1
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                end = min(len(words[i]), len(words[j]))
                m = 0
                for n in range(1, end+1):
                    if words[i].endswith(words[j][:n]):
                        m = n
                if m > m_1:
                    m_1 = m
                    i_1, j_1 = i, j
        full = words[i_1] + words[j_1][m_1:]
        w_1 = []
        for g in range(len(words)):
            if g != i_1 and g != j_1:
                w_1.append(words[g])
        w_1.append(full)
        words = w_1
    return words[0]

