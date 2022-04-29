import turtle
t = turtle.Turtle()
t.speed(100)
t.hideturtle()
t.color("green")

for i in range(100):
    t.circle(i)
    t._rotate(10)
