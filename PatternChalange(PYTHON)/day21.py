import turtle
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")
colour_of_flower=input("Enter color (red, 'blue, 'green, 'orange, 'purple,) : ")
#Drawing petals
t.color(colour_of_flower)
for i in range(36):
    t.circle(100)
    t.right(10)
#Drawing stem
t.penup()
t.goto(0, -100)
t.pendown()
t.color("green")
t.width(10)
t.right(90)
t.forward(200)
#Move to side for leaf
t.penup()
t.backward(100)   # move a bit up along the stem
t.right(80)       # rotate toward right side
t.forward(50)     # move slightly away from stem
t.pendown()
#Draw a tilted leaf
t.color("lightgreen")
t.begin_fill()
t.left(80)        # tilt the leaf
t.circle(40, 90)
t.left(90)
t.circle(40, 90)
t.end_fill()

t.hideturtle()
turtle.done()
