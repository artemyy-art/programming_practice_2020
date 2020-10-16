def power(a, n):
    if a == 1:
        return 1
    elif n == 0:
        return 1
    elif n > 0:
        return a * power(a, n - 1)
    else :
        if a > 1:
            if power(a, n-1) > 1:
                return 1/(a*power(a, n+1))
            else :
                return a*power(a, n+1)
        if a < 1:
            if power(a, n-1) > 1:
                return a*power(a, n+1)
            else :
                return 1/(a*power(a, n+1))
a=float(input())
n=float(input())
a=power(a, n)
print(a)
