import turtle

def draw_square(some_tutrle):
	for i in range(1,5):
		some_tutrle.forward(100)
		some_tutrle.right(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor('black')
	brad = turtle.Turtle()
	turtle.color("red")
	brad.color("red")
	brad.speed(10)
	brad.shape("turtle")
	for i in range(1,37):
		draw_square(brad)
		brad.right(10)
	#circle
	#angie = turtle.Turtle()
	#angie.color("blue")
	#angie.circle(45)
	window.exitonclick()
def draw_triangle():
	window = turtle.Screen()
	window.bgcolor("black")
	kj = turtle.Turtle()
	kj.color("red")
	kj.speed(1)
	for i in range(1,37):
		kj.forward(100)
		kj.right(90)
		kj.forward(200)
		kj.right(153.5)
		kj.forward(230)
	kj.right(324)
	kj.forward(300)
	window.exitonclick()
draw_triangle()