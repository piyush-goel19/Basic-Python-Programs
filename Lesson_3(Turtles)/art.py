import turtle
def triangle(turtle_1):
    for i in range(0,3):
        turtle_1.fd(200)
        turtle_1.right(120)
def art():
    window = turtle.Screen()
    window.bgcolor("white")

    pg = turtle.Turtle()
    pg.color("blue")
    pg.speed(5)
    pg.right(60)
    triangle(pg)
    pg.fd(100)
    pg.right(120)
   # triangle(pg)

    window.exitonclick()

art()
