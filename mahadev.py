import turtle as t

t.Screen() 
t.bgcolor('black')

def border():
    t.penup()
    t.pencolor("green")
    t.pensize(3)
    t.setposition(-250,-250)
    t.pendown()

    for i in range(1):
        t.forward(550)
        t.left(90)
        t.forward(450)
        t.left(90)
        t.forward(550)
        t.left(90)
        t.forward(450)

def lefteye():
    t.penup()
    t.pencolor("yellow")
    t.pensize(1)
    t.setposition(-100,50)
    t.pendown()
    a=10
    b=50
    t.circle(a,45)
    t.circle(b,90)
    t.circle(a,90)
    t.circle(b,90)
    t.circle(a,45)
    t.setposition(-85,50)
    t.left(90)
    t.forward(60)
    t.setposition(-85,50)
    t.right(90)
    t.circle(20,180)

def righteye():
    t.penup()
    t.pencolor("yellow")
    t.pensize(1)
    t.setposition(100,50)
    t.pendown()
    a=10
    b=50
    t.circle(a,45)
    t.circle(b,90)
    t.circle(a,90)
    t.circle(b,90)
    t.circle(a,45)
    t.circle(5,90)
    t.setposition(100,50)
    t.left(180)
    t.backward(75)
    t.setposition(40,50)
    t.right(90)
    t.circle(20,180)

def tilak():
    t.penup()
    t.setposition(50,90)
    t.pendown()
    t.left(-90)
    t.backward(100)
    t.left(360)
    t.circle(10,-180)
    t.left(180)
    t.forward(100)
    t.left(180)
    t.circle(10,-180)
    t.penup()
    t.setposition(-50,110)
    t.pendown()
    t.left(360)
    t.circle(10,-180)
    t.backward(100)
    t.right(-360)
    t.circle(10,-180)

def nose():
    t.penup()
    t.setposition(-10,-10)
    t.pendown()
    t.left(180)
    t.circle(10,180)
    t.left(-90)
    t.circle(10,180)
    t.left(-90)
    t.circle(10,180)

def lips():
    t.penup()
    t.setposition(0,-70)
    t.pendown()
    t.left(90)
    t.circle(10,-140)
    t.left(90)
    t.setposition(40,-75)
    t.penup()
    t.setposition(0,-63)
    t.pendown()
    t.left(-90)
    t.circle(10,95)
    t.left(-90)
    t.setposition(-40,-75)
    t.left(180)
    t.setposition(40,-75)
    t.setposition(0,-95)
    t.setposition(-40,-75)
    


border()
lefteye()
righteye()
tilak()
nose()
lips()

t.done()