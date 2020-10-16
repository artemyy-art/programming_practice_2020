def func(x):
    if -5 <= x <= 5:
        return x * x
    elif x < -5:
        return 2 * abs(x) - 1
    else:
        return 2 * x
print(func(int(input())))
