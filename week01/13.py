import turtle as t
t.shape('turtle')
def stars(n):
    for i in range(n + 1):
        t.left(180 - (180 / n))
        t.forward(100)
t.penup()
t.goto(-300,0)
t.pendown()
stars(5)
t.penup()
t.goto(300,0)
t.pendown()
stars(11)

