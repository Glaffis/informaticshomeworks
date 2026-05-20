def prefix(s):
    p = [0] * len(s)
    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[k] != s[i]:
            k = p[k - 1]
        if s[k] == s[i]:
            k += 1
        p[i] = k
    return p
def z_function(S):
    zf = [0]*len(S)
    left, right = 0, 0
    for i in range(1, len(S)):
        zf[i] = max(0, min(zf[i - left], right - i))
        while i + zf[i] < len(S) and S[zf[i]] == S[i + zf[i]]:
            zf[i] += 1
        if i + zf[i] > right:
            left, right = i, i + zf[i]
    return zf

def prefix_to_z(p):
    n = len(p)
    s = [''] * n
    s[0] = 'a'
    next_char = 'b' 
    for i in range(1, n):
        if p[i] > 0:
            s[i] = s[p[i] - 1]
        else:
            s[i] = next_char
            next_char = chr(ord(next_char) + 1)
    return z_function(''.join(s))

def z_to_prefix(z):
    n = len(z)
    s = [''] * n
    s[0] = 'a'
    next_char = 'b'
    for i in range(1, n):
        if z[i] > 0:
            for k in range(z[i]):
                if s[i + k] == '':
                    s[i + k] = s[k]
        if s[i] == '':
            s[i] = next_char
            next_char = chr(ord(next_char) + 1)
    return prefix(''.join(s))