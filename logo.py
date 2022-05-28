from time import sleep
import turtle
from unicodedata import name
def nessy():
    turtle.color('red')
    style = ('Arial Black', 50, 'italic')
    turtle.write('Newssy\n', font=style, align='center')
    
#turtle.hideturtle()

    t = turtle.Turtle()
    t.speed(2)
    turtle.bgcolor("black")
    t.color("black")
    turtle.title('Welcome logo')
    t.up()
    t.goto(-80, 50)
    t.down()
    t.fillcolor("black")
    t.begin_fill()
    t.forward(200)
    t.setheading(270)
    s = 360
    for i in range(9):
      s = s - 10
      t.setheading(s)
      t.forward(10)

    t.forward(180)
    s = 270
    for i in range(9):
       s = s - 10
       t.setheading(s)
       t.forward(10)

    t.forward(200)
    s = 180
    for i in range(9):
       s = s - 10
       t.setheading(s)
       t.forward(10)

    t.forward(180)
    s = 90
    for i in range(9):
       s = s - 10
       t.setheading(s)
       t.forward(10)
    t.forward(30)
    t.end_fill()
    t.up()
    t.color("black")
    t.setheading(270)
    t.forward(240)
    t.setheading(0)
    t.down()
    t.color("#66FF00")
    t.fillcolor("#66FF00")
    t.begin_fill()
    t.forward(30)
    t.setheading(90)
    t.forward(180)
    t.setheading(180)
    t.forward(30)
    t.setheading(270)
    t.forward(180)
    t.end_fill() 
    t.setheading(0)
    t.up()
    t.forward(75)
    t.down()
    t.color("#66FF00")
    t.fillcolor("#66FF00")
    t.begin_fill()
    t.forward(30)
    t.setheading(90)
    t.forward(180)
    t.setheading(180)
    t.forward(30)
    t.setheading(270)
    t.forward(180)
    t.end_fill()
    t.color("#66FF00")
    t.fillcolor("#66FF00")
    t.begin_fill()
    t.setheading(113)
    t.forward(195)
    t.setheading(0)
    t.forward(31)
    t.setheading(293)
    t.forward(196)
    t.end_fill()
    t.hideturtle()
    sleep(4)

    turtle.exitonclick()