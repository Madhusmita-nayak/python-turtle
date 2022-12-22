import turtle

winn = turtle.Screen()
turtle.bgcolor('black')
t = turtle.Turtle()
colors = ['red','dark red']
for i in range(400):
    t.forward(i+1)
    t.right(89)
    t.pencolor(colors[i%2])
turtle.done()
