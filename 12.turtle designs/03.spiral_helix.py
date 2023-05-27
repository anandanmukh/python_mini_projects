#python program to draw spiral helix using turtle programming

import turtle

loadWindow=turtle.Screen()

turtle.speed(2)

turtle.bgcolor("black")
for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5 * i)
    turtle.left(i)

turtle.exitonclick()