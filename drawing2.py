import turtle as tur
import colorsys as cs

tur.setup(800,800)
tur.speed(10)
tur.tracer(10)
tur.width(1)
tur.bgcolor('black')
for j in range(25):
    for i in range(15):
        tur.color(cs.hsv_to_rgb(i/15,j/15,1))
        tur.left(45)
        tur.circle(30+j*6,360);


tur.hideturtle()
tur.done()