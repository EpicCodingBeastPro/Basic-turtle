import turtle

t=turtle.Pen()
s=turtle.Screen()

s.title("Rectangle with traingle")
t.pensize(4)
s.screensize(bg='black')

t.pencolor("white")

def rotate():
	t.left(120)
	t.forward(110)
	
rotate()
rotate()
rotate()

turtle.done()
