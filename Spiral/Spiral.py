import turtle as t
#we can change the colors and the number of sides depending on our personal intrest
t.bgcolor("black")
t.speed(10)
sides=6
colors=["red","yellow","green","blue","orange","purple"]
for x in range(150):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides+x)
    t.left(360/sides+1)
    t.width(x*sides/200)
t.exitonclick()