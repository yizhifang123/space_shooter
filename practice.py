import turtle
import calendar

yili_turtle = turtle.Turtle()
yili_turtle.speed(100000000000000000000000000000000000000)

# dis is a square
# yili_turtle.forward(100)
# yili_turtle.right(90)
# yili_turtle.forward(100)
# yili_turtle.right(90)
# yili_turtle.forward(100)
# yili_turtle.right(90)
# yili_turtle.forward(100)
# yili_turtle.right(90)

def square():
    yili_turtle.forward(100)
    yili_turtle.right(90)
    yili_turtle.forward(100)
    yili_turtle.right(90)
    yili_turtle.forward(100)
    yili_turtle.right(90)
    yili_turtle.forward(100)

def triangle():
    yili_turtle.left(115)
    yili_turtle.forward(100)
    yili_turtle.left(115)
    yili_turtle.forward(120)
    yili_turtle.left(130)
    yili_turtle.forward(120)


# square()
# square()

# print(calendar.month(2020, 11))
# print(calendar.calendar(2020))

# is_leap = calendar.isleap(2020)
# print(is_leap)

# how_many_leap_days = calendar.leapdays(2000, 2100000000)
# print(how_many_leap_days)

# elephant = 100
# ant = 1

# if elephant > ant:
    # square()
# else:
    # print("ur stupid")

# while elephant > ant:
    # square()
    # yili_turtle.forward(100)
    # yili_turtle.left(45)
    # ant + 1

for i in range(0, 100):
    triangle()
    square()
    yili_turtle.forward(100)
    yili_turtle.left(115)
