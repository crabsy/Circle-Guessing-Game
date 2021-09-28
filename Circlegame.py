import turtle
import random
import math

rows = 8
columns = 8
coords = turtle.position()
x = coords[0]
y = coords[1]

graycircle_list=[]
redcircle_list=[]

turtle.color("gray")
turtle.resetscreen
turtle.setworldcoordinates(-1,-1,8,8)
turtle.hideturtle
incorrect = 0

for n in range(columns):
    turtle.speed(0)
    turtle.penup()
    turtle.setpos(0,0)
    turtle.sety(y)
    y = y + 1
    colorfulfilled = 0
    for n in range(rows):
        color = random.randint(0,2)
        turtle.color('gray')
        if color == 1 and colorfulfilled == 0:
            turtle.color('gray') #circles that blow up
            center = turtle.position()
            turtle.begin_fill()
            turtle.circle(0.5)
            turtle.forward(1)
            turtle.end_fill()
            redcircle_list.append(center)
            colorfulfilled = 1
            redcircle_list.append(center)
        else:
            turtle.color('gray')
            center = turtle.position()
            turtle.begin_fill()
            turtle.circle(0.5)
            turtle.forward(1)
            turtle.end_fill()
            graycircle_list.append(center)


redm_circle = random.choice(redcircle_list)
redm_circle = str(redm_circle)
redm_circle = redm_circle.replace("(","")
redm_circle = redm_circle.replace(")","")
e,d = redm_circle.split(",", 1)
e = float(e)
d = float(d)


m_circle = random.choice(graycircle_list)
m_circle = str(m_circle)
m_circle = m_circle.replace("(","")
m_circle = m_circle.replace(")","")
f,g = m_circle.split(",", 1)
f = float(f)
g = float(g)
print(int(f))
print(int(g))

print(redm_circle)
print(m_circle)

ystart=4.5
num = 4
for n in range(8):
    turtle.goto(-1,ystart)
    turtle.write(num)
    ystart = ystart - 1
    num = num - 1
xstart = 4
num2 = 4
for n in range(8):
    turtle.goto(xstart, -1)
    turtle.write(num2)
    xstart = xstart - 1
    num2 = num2 - 1

while True:
    userguess = turtle.textinput("Circle", "Format: x,y")
    a,b = userguess.split(",", 1)
    a = int(a)
    b = int(b)

    if a > 4:
        print("Thats too high! The board only goes to 4!")
        turtle.goto(0,5.5)
        turtle.write("Thats too high! The board only goes to 4!", align = "left")
    if b > 4:
        print("Thats too high! The board only goes to 4!")
        turtle.goto(0,5.5)
        turtle.write("Thats too high! The board only goes to 4!", align = "left")
    if a != f and b != g or a != e and b != d:
        turtle.penup()
        turtle.goto(a,b)
        turtle.color('white')
        turtle.begin_fill()
        turtle.circle(0.5)
        turtle.end_fill()
        incorrect = incorrect + 1
        print(incorrect)
    if a != f and b == g:
        turtle.penup() 
        turtle.goto(a,b)
        turtle.color('white')
        turtle.begin_fill()
        turtle.circle(0.5)
        turtle.end_fill()
        incorrect = incorrect + 1
        print(incorrect)
    if a == f and b !=g:
        turtle.penup()
        turtle.goto(a,b)
        turtle.color('white')
        turtle.begin_fill()
        turtle.circle(0.5)
        turtle.end_fill()
        incorrect = incorrect + 1
        print(incorrect)
    if a == f and b == g:
        turtle.penup()
        turtle.setpos(f,g)
        turtle.color('green')
        turtle.begin_fill()
        turtle.circle(0.5)
        turtle.end_fill()
        turtle.goto(0,5)
        turtle.write("Congratulations, you found the mystery circle!", font=("Arial", 8, "normal"))
        turtle.delay(10)
        turtle.bye()
    if a == e and b == d:
        turtle.penup()
        turtle.setpos(e,d)
        turtle.color('black')
        turtle.begin_fill()
        turtle.circle(0.5)
        turtle.end_fill()
        turtle.goto(0,5)
        turtle.write("YOU LOST", font=("Arial", 8, "normal"))
        turtle.delay(10)
        turtle.bye()
