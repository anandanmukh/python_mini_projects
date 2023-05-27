#drawing rainbow benzene using python turtle programming

import turtle
#loadWindow=turtle.Screen()
#turtle.speed(2)
colors=['red','purple','blue','green','orange','yellow']
t=turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)

turtle.exitonclick()