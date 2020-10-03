import turtle as t
n=int(input())
for i in range(n+1):
    t.forward(100)
    t.backward(100)
    t.left(360/n)
