a = [1, 2, 3, 4, 5, 6]
b = [4, 5, 6, 7, 8, 9]

A = set(a)
B = set(b)

unique_each = A.symmetric_difference(B)
unique_union = A.union(B)
common = A.intersection(B)

print("Уникальные для каждого списка:", unique_each)
print("Уникальные для объединения:", unique_union)
print("Содержащиеся в обоих списках:", common)
