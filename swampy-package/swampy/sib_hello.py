# Hello excercise from Week 0

# Name:


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				

# This is where you put code to move bob

#Functions

#pen-down moves
def draw_1 (bob, n):
	pd(bob)
	fd(bob,n)

def draw_2 (bob, n):
	for i in range(2):
		draw_1 (bob, n)

def draw_1_lt (bob,n):
	draw_1(bob, n)
	lt(bob)

def draw_2_lt (bob, n):
	draw_2 (bob, n)
	lt(bob)

#pen-up moves
def move_long (bob, n):
	pu(bob)
	fd(bob, n)

def move_long_lt(bob, n):
	pu(bob)
	fd(bob, n)
	lt(bob)

def move_short (bob, n):
	pu(bob)
	fd(bob, 3)

def move_short_rt(bob, n):
	pu(bob)
	fd(bob, 3)
	rt(bob)

def twirl (bob):
	for i in range (6):
		rt(bob)

#letters 
def L (bob,n):
	draw_2_lt(bob,n)
	draw_1_lt(bob, n)
	for i in range(2):
		move_long(bob, n)
	rt(bob)
	move_short_rt(bob, n)

def O (bob, n):
	draw_2_lt(bob, n)
	draw_1_lt(bob, n)
	draw_2_lt(bob,n)
	draw_1(bob, n)

def span_LL (bob, n):
	for i in range(2):
		move_short(bob,n)
		move_long (bob, n)
	move_short(bob,n)

def E_H (bob, n):
	draw_1_lt (bob, n)
	draw_2(bob, n)
	rt (bob)
	move_short_rt(bob,n)
	draw_2_lt(bob, n)
	move_long_lt (bob,n)
	draw_2_lt(bob, n)
	move_long(bob, n)
	move_short(bob,n)
	draw_1_lt(bob, n)
	move_long_lt (bob, n)
	draw_1(bob, n)
	move_short(bob, n)
	draw_1(bob, n)


#CALLS

#positions turtle 
rt(bob)

#draws the word HELLO
L(bob, 10)
L(bob, 10)
O(bob, 10)
span_LL(bob, 10)
E_H (bob, 10)

#victory dance
pu(bob)
fd(bob, 20)
twirl(bob)


wait_for_user()					
