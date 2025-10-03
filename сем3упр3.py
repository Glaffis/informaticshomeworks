def gcdext(a, b):
    if b == 0:
        d, x, y = a, 1, 0
        return d, x, y
    d, x1, y1 = gcdext(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return d, x, y
if __name__ == "__main__":
    while True:
        line = input().strip()
        if not line:    
            break
        a, b = map(int, line.split())
        d, x, y = gcdext(a, b)
        print(x, y, d)