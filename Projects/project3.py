import turtle
#this is where the code starts
turtle.Screen().bgcolor("black")
t = turtle.Turtle()

t.goto(0,0)
colors = ["green","hotpink"]

#this is where I choose my colors
for i in range (5):
    t.color ( colors[i % 2] )
    t.forward(1)
    t.left (72)
    t.speed(10)


for i in range ( 500 ):
    t.color ( colors[i % 2] )
    t.forward( 1 + i)
    #this is where I dictate speed,color and movement
    t.left (72 + 1)
    t.speed(10)


turtle.exitonclick ()