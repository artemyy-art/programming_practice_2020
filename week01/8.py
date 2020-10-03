import turtle
import math
t = turtle.Turtle()
t.shape('turtle')
R = 10
x = 1
n = 3
t.up()
t.goto(R, 0)
t.down()
def p(x):
    for i in range(n+1):
        t.left((180+360 / n) / 2)
        t.forward(2 * R * math.sin(math.pi/n))
        x += 1
        t.right((180 - 360 / n) / 2)
for n in range(3,15,1):
    p(n)
    R += 10
    t.up()
    t.goto(R, 0)
    t.down()
