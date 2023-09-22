from turtle import*
hideturtle()
color('red')
begin_fill()

for x in(230, 120, 230, 120):
    forward(x)
    circle(40, 90)
end_fill()

up()
goto(80, 50)
down()
color('white')
begin_fill()
for x in(30,120,120):
    left(x)
    forward(100)
end_fill()

up()
goto(-10,-100)
down()
pencolor('black')
write("YouTube","center", font=("Arial", 40,"bold"))
done()