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

left(90)
forward(450)
color('yellow')
begin_fill()
left(90)
circle(200,180)
end_fill()

left(90)
forward(350)
color('green')
begin_fill()
left(90)
circle(150,180)
end_fill()

left(90)
forward(250)
color('blue')
begin_fill()
left(90)
circle(100,180)
end_fill()

left(90)
forward(150)
color('purple')
begin_fill()
left(90)
circle(50,180)
end_fill()

left(90)
forward(60)
color('cyan')
begin_fill()
left(90)
circle(10,360)
end_fill()



exitonclick()
