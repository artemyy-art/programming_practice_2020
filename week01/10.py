import turtle as t
t.right(90)
for i in range(10):
    t.circle(i*10)
    t.penup()
    t.right(90)
    t.forward(i*20)
    t.left(90)
    t.pendown()
    t.circle(i*10)
    t.penup()
    t.right(90)
    t.backward(i*20)
    t.left(90)
    t.pendown()