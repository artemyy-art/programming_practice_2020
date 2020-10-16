import math
def circle(r):
    return math.pi * r ** 2
def rectangle(a, b):
    return a * b
def triangle(a, b, c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return s
choice = input("круг(к), прямоугольник(п) или треугольник(т): ")
if choice == 'к':
    r = float(input("радиус: "))
    print("площадь:" , circle(r))
elif choice == 'п':
    l, w = [int(s) for s in input("длина и ширина через пробел ").split()]
    print("площадь:" , rectangle(l, w))
elif choice == 'т':
    a, b, c = [int(s) for s in input('три стороны через пробел ').split()]
    print("площадь: " ,triangle(a, b, c))