from turtle import *


#we want to paint a house

#step 1:  draw a square
speed(30)
width(7)
color("gray")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square :)

#drawing a door

forward(70)
begin_fill()
color("black")
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing windows :3

left(30)
begin_fill()
color("gray")
forward(80)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
end_fill()

penup()
goto(200, 200)
pendown()

left(90)
begin_fill()
forward(80)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()

exitonclick()

