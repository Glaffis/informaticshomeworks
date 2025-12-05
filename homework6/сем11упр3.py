import random

def QuickSort(A):
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = []
        M = []
        R = []
        for elem in A:
            if elem < q:
                L.append(elem) 
            elif elem > q: 
                R.append(elem) 
            else: 
                M.append(elem)
        return QuickSort(L) + M + QuickSort(R)
        

assert QuickSort([]) == [], "Error: список пуст"
assert QuickSort([1]) == [1], "Error: только один элемент"
assert QuickSort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Error: список уже отсортирован"
assert QuickSort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5], "Error: обратный список"
assert QuickSort([1, 4, 6, 1, 3, 4]) == [1, 1, 3, 4, 4, 6], "Error: случайный список"
assert QuickSort([1,1,1]) == [1,1,1], "Error: одни и те же элементы"
assert QuickSort([-3, -2, -1]) == [-3, -2, -1], "Error: отрицательные числа"
large = list(range(100))
random.shuffle(large)
sorted_large = QuickSort(large.copy()) 
assert sorted_large == list(range(100)), "Error: большой случайный список"
assert QuickSort([1.1, 1.2, 1.3]) == [1.1, 1.2, 1.3], "Error: числа не целые"


print("Код верный")