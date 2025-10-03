def make_triangle(strk, symb):
    if strk%2 != 0:
        the_longest=strk//2 + 1
        for i in range(0, the_longest):
            print(symb*i)
        for j in range(the_longest, 0, -1):
            print(symb*j)
    else:
        the_longest = strk//2
        for i in range(1, the_longest+1):
            print(symb*i)
        for j in range(the_longest, 0, -1):
            print(symb*j)
        
make_triangle(7, '%') #пример