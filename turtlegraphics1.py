import turtle as tu
t=tu.Turtle()
s=tu.Screen()
s.bgcolor('red')
t.width(3)
t.speed(30)
col = ('green', 'blue', 'black')
for i in range (200):
    t.pencolor(col[i%3])
    t.forward(i*4)
    t.right(122)