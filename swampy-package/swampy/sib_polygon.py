# Polygon excercise from Week 0

# Name:


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				

# This is where you put code to move bob

#FUNCITONS

#draws line segment
def line(bob, n):
	pd(bob)
	fd(bob, n)

#moves one line segment w/o drawing
def move(bob, n):
	pu(bob)
	fd(bob, n)

#creates a circle
def cir(bob, n, a):
	pd (bob)
	fd(bob, n)
	rt(bob, a)

#creates the letter h
def h(bob, n):
	line(bob, n)
	line(bob, n)
	rt(bob, 180)
	move(bob, n)
	rt(bob)
	line(bob, n)
	lt(bob, 90)
	line(bob, n)
	rt(bob, 180)
	line(bob, n)
	line(bob, n)
	rt(bob, 180)
	move(bob, n)
	rt(bob)


#creates the letter E
def e_half (bob, n):
	for i in range(3):
		fd(bob, n)
		lt(bob)

def e (bob, n):
	e_half(bob, n)
	lt(bob, 90)
	e_half(bob, n)

#creates the letter L
def l(bob, n):
	move (bob, 10)
	for i in range(2):
		line(bob, n)
	lt(bob)
	line(bob, n)
	lt(bob)
	for i in range(2):
		move(bob, 50)
	rt(bob, 180)




#CALLS

#positions and prints first letter
pu(bob)
bk(bob, 150)
lt(bob)
fd(bob, 75)
rt(bob, 180)
pd(bob)

h (bob, 50)

#positions and prints second letter 
move(bob, 10)
lt(bob)
fd(bob, 50)
rt(bob)
move(bob, 50)
rt(bob, 180)
pd(bob)

e (bob, 50)

#positions and prints third and fourth letters 

move(bob, 100)
rt(bob, 180)

l(bob, 50)


wait_for_user()					
