import turtle

#triangle
turtle.right(225)
turtle.forward(100)
turtle.left(225)
turtle.forward(140)
turtle.left(225)
turtle.forward(100)

turtle.left(135)
turtle.up()
turtle.forward(200)
turtle.down()

#carré
turtle.begin_fill()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.end_fill()

turtle.up()
turtle.forward(200)
turtle.down()

#rond
turtle.circle(50,180)

turtle.exitonclick()
