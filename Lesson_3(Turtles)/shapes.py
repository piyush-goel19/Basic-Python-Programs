import turtle
def shapes():
    window = turtle.Screen()
    window.bgcolor("cyan")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.speed(4)
    for i in range(0,4):
        brad.fd(100)
        brad.right(90)
    ayu = turtle.Turtle()
    ayu.shape("circle")
    ayu.color("black")
    ayu.speed(4)
    ayu.circle(100,180)
    turtle.home()
    pg = turtle.Turtle()
    pg.shape("triangle")
    pg.color("blue")
    pg.speed(4)
    for i in range(0,3):
        pg.backward(200)
        pg.lt(120)
    window.exitonclick()

shapes()


    
