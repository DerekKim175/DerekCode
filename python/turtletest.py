import turtle
import time
import random

t = turtle.Turtle()

t.shape('turtle')

t.speed(0)

# def star():

# 		for i in range(5):

# 			t.right(144)

# 			t.forward(100)

# x = 10

# while x > 5:

# 	x -= 1

# 	star()

# 	t.penup()

# 	t.setx(random.randint(-200,200))

# 	t.sety(random.randint(-200,200))

# 	t.pendown()

def circle1(x,y,z):
	t.color(x)

	t.pensize(5)

	t.penup()
	t.setx(y)
	t.sety(z)
	t.pendown()
	t.circle(50)

	# t.color('green')

	# t.pensize(5)

	# t.penup()
	# t.setx(100)
	# t.sety(30)
	# t.pendown()
	# t.circle(50)

	# t.color('black')

	# t.pensize(5)

	# t.penup()
	# t.setx(50)
	# t.sety(100)
	# t.pendown()
	# t.circle(50)

	# t.color('yellow')

	# t.pensize(5)

	# t.penup()
	# t.setx(0)
	# t.sety(30)
	# t.pendown()
	# t.circle(50)

	# t.color('blue')

	# t.pensize(5)

	# t.penup()
	# t.setx(-50)
	# t.sety(100)
	# t.pendown()
	# t.circle(50)

# circle1('red',150,100

t.sety(100)
t.setx(100)
t.right(30)
t.penup()
t.setx(-200)
t.pendown()

t.right(90)


t.color('red')

t.begin_fill()

t.circle(100,180)

t.circle(-100,180)

t.left(180)
t.circle(200,180)

t.end_fill()


t.color('blue')

t.begin_fill()

t.circle(100,180)

t.circle(-100,180)
t.circle(-200,180)

t.end_fill()



time.sleep(10)
