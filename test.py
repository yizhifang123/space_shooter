from turtle import *
color('blue', 'gray')
begin_fill()
while True:
    forward(180)
    left(230)
    right(10)
    forward(150)
    left(50)
    forward(2)
    if abs(pos()) < 10:
        break
hideturtle()
end_fill()
done()
