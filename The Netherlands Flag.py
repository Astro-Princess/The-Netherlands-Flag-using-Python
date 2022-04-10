from turtle import *

speed(0)
setup(800, 500)

penup()
goto(-400, 250)
pendown()

color("#AE1C28")
begin_fill()
forward(800)
right(90)
forward(167)
right(90)
forward(800)
end_fill()

left(90)
forward(167)

color("#21468B")
begin_fill()
forward(167)
left(90)
forward(800)
left(90)
forward(167)
end_fill()

hideturtle()
