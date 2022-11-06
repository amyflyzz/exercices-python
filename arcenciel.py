from turtle import *

# The below code draws a raimbow



bgcolor('aqua')
speed(5)
up()
forward(300)
down()


color('red')
begin_fill()
left(90)
circle(300,180)
end_fill()
left(90)
forward(550)
color('orange')
begin_fill()
left(90)
circle(250,180)
end_fill()


def trace_un_bout_de_arcenciel(distance, couleur, radius, extent = 180) :
    left(90)
    forward(distance)
    color(couleur)
    begin_fill()
    left(90)
    circle(radius,extent)
    end_fill()

trace_un_bout_de_arcenciel(450, "yellow", 200)


trace_un_bout_de_arcenciel(350, "green", 150)

trace_un_bout_de_arcenciel(250, "blue", 100)

trace_un_bout_de_arcenciel(150, "purple", 50)

trace_un_bout_de_arcenciel(60, "cyan", 10, 360)



exitonclick()
