import turtle as t
t.speed(10)
t.hideturtle()
t.pu()
t.goto(-300,100)
t.pd()
t.bgcolor("blue")
t.color("white")
def min_star():
    for i in range(5):
        t.fd(10)
        t.right(144)
def pattern():
    for i in range(5):
        min_star()
        t.fd(120)
        t.right(144)
def pattern2():
    for i in range(5):
        pattern()
        t.fd(700)
        t.right(144)
        

pattern2()
t.done()