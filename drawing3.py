import turtle as tur
import colorsys as cs

tur.setup(800,800)
tur.speed(2)
tur.width(1)
tur.bgcolor('black')
for j in range(25):
    for i in range(15):
        tur.color(cs.hsv_to_rgb(i/15,j/15,1))
        tur.forward(i*5)
        tur.right(45)

tur.penup()
tur.setposition(0,0)
tur.pendown()
tur.done()