f = open('input.txt','r',encoding='utf-8')
s = f.readline()
glas = 'ауоиыяюеёэАУОИЫЯЮЕЁЭ'
r = ''
i = int()
while i<(len(s)):
    if i==0:
        i+=1
        if s[i] in glas: r = s[i]
        continue
    elif i==len(s)-1:
        if s[i] in glas: s = s[:i+1]+'с'+s[i]
        break
    elif (s[i] in glas and s[i-1] not in glas and s[i+1] not in glas):
        if s[i] in glas: r = s[i]
        s = s[:i+1]+'с'+r+s[i+1:]
        i+=2
    elif s[i] in glas and s[i-1] not in glas and s[i+1] in glas:
        if s[i] in glas: r = s[i]
        s = s[:i+1]+'с'+r+s[i+1:]
        i+=2
    i+=1
print(s)