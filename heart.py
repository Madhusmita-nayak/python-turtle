import turtle as tur
import time 

tur.setup(800,800)
tur.speed(2)
tur.width(5)
tur.bgcolor('black')

tur.color('red')
tur.begin_fill()
tur.pencolor('darkred')
tur.penup()
tur.setposition(50,100)
tur.pendown()
tur.left(40)
tur.circle(90,200)
tur.right(100)
tur.circle(90,200)
tur.goto(-50,0)
tur.goto(50,100)
tur.end_fill()

tur.penup()  
tur.pencolor("white")
tur.setposition(-80,130)
tur.pendown()
tur.write('Madhu',move=False,align='center',font=('Arial',18,'normal'))

tur.mainloop()
tur.done()