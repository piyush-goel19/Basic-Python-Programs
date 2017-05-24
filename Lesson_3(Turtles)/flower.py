import turtle

def draw_triangle(turtle_1):
    turtle_1.fd(60)
    turtle_1.right(60)
    turtle_1.fd(60)
    turtle_1.right(120)
    turtle_1.fd(60)
    turtle_1.right(60)
    turtle_1.fd(60)
    
def flower():
    window = turtle.Screen()
    window.bgcolor("yellow")
    pg = turtle.Turtle()
    pg.shape("triangle")
    pg.color("red")
    pg.speed(8)
    for i in range(1,73):
        draw_triangle(pg)
        pg.right(5)
  #  pg.pu()
  #  pg.goto(56,-25)
  #  pg.pd()
    pg.right(90)
    pg.fd(150)
    window.exitonclick()

flower()
