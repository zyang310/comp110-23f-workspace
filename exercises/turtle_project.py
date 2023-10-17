"""Using Turtles to Create Art."""

__author__ = "730713735"

from turtle import Turtle, colormode, done, bgcolor
rammus: Turtle = Turtle()
rammus.speed(50)
colormode(255)
pen_width = 5
bgcolor(13, 23, 32)


def main() -> None:
    """Main functions where everything comes together."""
    # Modify the x and y value to move the whole thing around.
    x: int = -25
    y: int = 0

    rammus.fillcolor(227, 27, 35)
    rammus.begin_fill()
    heart(rammus, x, y)
    rammus.end_fill()
    
    letter_i(rammus, x, y)

    rammus.color(0, 0, 0)
    rammus.fillcolor(255, 215, 0)
    rammus.begin_fill()
    circle(rammus, x + (250), y + (-130), 190, 360)
    rammus.end_fill()

    rammus.fillcolor(63, 175, 180)
    rammus.begin_fill()
    circle(rammus, x + (250), y + (-100), 160, 360)
    rammus.end_fill()

    rammus.fillcolor(255, 215, 0)
    rammus.begin_fill()
    league_letter_L(rammus, x + (100), y + (260))
    rammus.end_fill()

    rammus.right(-15)
    rammus.hideturtle()

    done()


def circle(a_turtle: Turtle, x_cord: int, y_cord: int, radius: int, degree: int) -> None:
    """This functions draws a circle at a coordinate with the given radius and degree."""
    a_turtle.penup()
    a_turtle.goto(x_cord, y_cord)
    a_turtle.width(pen_width)
    a_turtle.pendown()
    a_turtle.circle(radius, degree)


def league_letter_L(a_turtle: Turtle, x_cord: int, y_cord: int) -> None:
    """This function draws the letter 'L' in the logo."""
    a_turtle.penup()
    a_turtle.goto(x_cord, y_cord)
    a_turtle.width(pen_width)
    a_turtle.pendown()
    line(rammus, 100.0, 90)
    line(rammus, 350.0, 270)
    line(rammus, 200.0, 135)
    line(rammus, 75.0, 45)
    line(rammus, 247.0, 135)
    line(rammus, 45.0, 315)
    line(rammus, 340.0, 315)
    line(rammus, 44.5, 150)
 

def line(a_turtle: Turtle, length: float, angle: int) -> None:
    """This function justs draws a line and then turns in the appropirate direction."""
    a_turtle.forward(length)
    a_turtle.right(angle)


def letter_i(a_turtle: Turtle, x_cord: int, y_cord: int) -> None:
    """This functions uses the rectangles to draw the Letter "I"."""
    a_turtle.color(255, 255, 255)
    rectangle(a_turtle, x_cord + (-450), y_cord + (200), 200, 30)
    rectangle(a_turtle, x_cord + (-370), y_cord + (200), 30, 250)
    rectangle(a_turtle, x_cord + (-450), y_cord + (-50), 200, 30)


def heart(a_turtle: Turtle, x_cord: int, y_cord: int) -> None:
    """Draws a heart at the designated destination."""
    a_turtle.penup()
    a_turtle.goto(x_cord + (-100), y_cord + (-25))
    a_turtle.width(pen_width)
    a_turtle.pendown()

    a_turtle.color(227, 27, 35)
    a_turtle.left(140) 
    a_turtle.forward(113) 
    curve(a_turtle) 
    a_turtle.left(120)
    curve(a_turtle) 
    a_turtle.forward(112)
    a_turtle.right(220)


def rectangle(a_turtle: Turtle, x_cord: int, y_cord: int, width: int, length: int) -> None:
    """This functions draws rectangles at a designated coordinate and fill it with a color."""
    a_turtle.penup()
    a_turtle.goto(x_cord, y_cord)
    a_turtle.width(pen_width)
    a_turtle.pendown()
    
    counter: int = 0
    rammus.fillcolor(255, 255, 255)
    rammus.begin_fill()
    while counter < 2:
        rammus.forward(width)
        rammus.right(90)
        rammus.forward(length)
        rammus.right(90)
        counter = counter + 1
    rammus.end_fill()


def curve(a_turtle: Turtle) -> None:
    """Draw a curve for the heart."""
    counter = 0
    while counter < 200:
        a_turtle.right(1) 
        a_turtle.forward(1)
        counter = counter + 1


if __name__ == "__main__":
    main()