S = input()
a = list(S) 
n = 0
for i in range (len(a)-1): 
    if a[i] == '.' and a[i+1] == ' ':
        n +=1 
    elif a[i] == '!' and a[i+1] == ' ':
        n+=1 
    elif a[i] == '?' and a[i+1] == ' ':
        n+=1
print(n+1)