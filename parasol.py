#bidouillage1
import turtle 
turtle.bgcolor('sky blue')
#bidouillage1
turtle.up()
turtle.right(90)
turtle.forward(300)
turtle.down()
#baton
turtle.color('grey')
turtle.begin_fill()
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(300)
turtle.end_fill()
#bidouillage3
turtle.backward(300)
turtle.pensize("10")
#toile
turtle.color("orange")
turtle.begin_fill()
turtle.left(90)
turtle.forward(160)
turtle.left(90)
turtle.circle(150,180)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.end_fill()
turtle.pensize(13)
turtle.color('red')
turtle.backward(150)
turtle.left(90)
turtle.forward(35)
turtle.right(60)
turtle.forward(130)
turtle.backward(130)
turtle.right(120)
turtle.forward(70)
turtle.left(60)
turtle.forward(130)
turtle.backward(130)
turtle.right(60)
turtle.forward(60)
turtle.left(50)
turtle.forward(70)
turtle.backward(70)
turtle.left(130)
turtle.forward(190)
turtle.right(55)
turtle.forward(75)
turtle.backward(75)
turtle.right(125)
turtle.color('red')
turtle.forward(200)
turtle.backward(255)
turtle.right(90)
turtle.color('red')
#detail
for i in range(15) :
    turtle.speed(20)
    turtle.circle(10,180)
    turtle.right(180)
turtle.right(90)
turtle.forward(50)
turtle.backward(50)
turtle.color('red')
turtle.right(90)
turtle.circle(150,180)
turtle.up()
turtle.forward(300)
turtle.down()
#sable
turtle.color('gold')
turtle.begin_fill()
turtle.right(90)
turtle.forward(700)
turtle.left(90)
turtle.forward(120)
turtle.left(90)
turtle.forward(1650)
turtle.left(90)
turtle.forward(120)
turtle.left(90)
turtle.forward(1000)
turtle.end_fill()
#bidoillage4
turtle.exitonclick()