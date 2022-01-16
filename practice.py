from turtle import *

showturtle()
penup()
setpos(100,100)
pendown()

color('black')
style = ('Times', 40, 'bold')
write('Hello World!', font=style, align='center')

penup()
setpos(0,0)
pendown()
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()