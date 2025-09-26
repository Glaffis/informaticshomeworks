from collections import Counter
a = input().split()
element = Counter(a).most_common(1)[0][0]
print(element)