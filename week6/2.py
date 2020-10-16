def yjl(c, d):
    a=max(c, d)
    b=min(c,d)
    if a!=0 and b!=0:
        return yjl(a%b, b)

    return a+b
a=b=1
while a != 0 or b != 0:
    a = input("Two numbers: ")
    a = a.split()
    b = int(a[1])
    a = int(a[0])
    print(yjl(a, b))
