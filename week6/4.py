def diagonal(l,c):
    s = 0
    i = 0
    while i < n:
        if c == '1':
            s += l[i][i]
        else:
            s += l[i][N-i-1]
        i += 1
    return s
m = []
m.append(list(map(int,input().split())))
n = len(m[0])
k = 1
while k < n :
    m.append(list(map(int,input().split())))
    k += 1
ch = input("Главная (1) или побочная (2): ")
if ch == '1' or ch == '2':
    summa = diagonal(m,ch)
    print(summa)