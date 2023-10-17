from turtle import Turtle, colormode, done
oogway: Turtle = Turtle()
colormode(255)
side_length = 500

oogway.color(255,255,204)

oogway.penup()
oogway.goto(-250, -150)
oogway.pendown()

oogway.fillcolor(255,255,204)
oogway.begin_fill()
counter:int = 0
while counter < 3:
    oogway.forward(side_length)
    oogway.left(120)
    counter += 1
oogway.end_fill() 

oogway.pencolor("pink")

oogway.color("green", "yellow")




bob: Turtle = Turtle()
bob.speed(50)
bob.color(0,0,0)
bob.penup()
bob.goto(-250, -150)
bob.pendown()
counter: int = 0
while counter < 20:
    bob.forward(side_length)
    bob.left(121.2)
    side_length *=0.97
    counter += 1

done()