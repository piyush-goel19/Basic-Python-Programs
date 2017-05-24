import turtle
def square():
    window = turtle.Screen()
    window.bgcolor("cyan")
    pg = turtle.Turtle()
    pg.shape("turtle")
    pg.color("red")
    pg.speed(5)
    angle = 5
    count = 0
    while(count < 72):
        pg.forward(150)
        pg.right(90)
        pg.forward(150)
        pg.right(90)
        pg.forward(150)
        pg.right(90)
        pg.forward(150)
        pg.right(90)
        pg.right(angle)
        count = count + 1
    
    window.exitonclick()

square()
