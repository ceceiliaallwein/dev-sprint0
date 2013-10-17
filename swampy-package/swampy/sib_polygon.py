# Polygon excercise from Week 0

# Name: Ceceilia Allwein

# Note: Function calls commented out in order to select 

from TurtleWorld import * 		

world = TurtleWorld()			
bob = Turtle()				
bob.delay = .1


# This is where you put code to move bob

import math 

def square (t, l):
	'''moves turtle one line segment
	and pivots right the default angle'''
	for i in range (4):
		fd (t, l)
		rt (t)

#square (bob, 30)

def square_ref (t, n, l, a):
	''' draws n line segments + turns with 
	given side length and angles. t is the turtle'''
	for i in range (n):
		fd (t, l)
		rt (t, a)

def polygon (t, n, l): 
	''' determines the angle of the turn 
	based on the given number of sides'''
	a = 360 / n
	square_ref (t, n, l, a)

#polygon (bob, 10, 8)

def circle (t, r):
	'''draws an approximate circle; relates 
	the number of sides and the length of 
	those sides to the circumference of the 
	circle with a given radius'''
	circumference = 2 * math.pi * r
	n = r
	l = circumference / n 
	polygon (t, n, l)

#circle (bob, 10)

def move_turtle (turtle, no_sides, seg_length, angle):
	''' 
	In the text this is called polyline. 
	Moves (without drawing) line segments 
	+ turns similar to square or square_ref 
	'''
	pu (turtle)
	for i in range (no_sides):
		fd (turtle, seg_length)
		rt (turtle, angle)
	pd (turtle)

def line_subtend (turtle, no_sides, seg_length, angle):
	''' 
	In the text this is called polyline. 
	Moves and draws line segments + turns 
	similar to square or square_ref 
	'''
	pd (turtle)
	for i in range (no_sides):
		pd (turtle)
		fd (turtle, seg_length)
		rt (turtle, angle)

def polygon (turtle, no_sides, seg_length): 
	''' 
	Determines the angle of the turn in 
	line_subtend based on the number 
	of sides
	'''
	angle = 360.0 / no_sides
	line_subtend (turtle, no_sides, seg_length, angle)

def arc (turtle, radius, angle):
	'''
	writes only a portion of the circumference 
	of a circle, with a given radius and 
	angle that the arc subtends 
	''' 
	seg_length = 2 * math.pi * radius * angle / 360
	no_sides = int(seg_length / radius)
	draw_length = float(seg_length / no_sides)
	angle_subtend_deg = angle / no_sides
	line_subtend (turtle, no_sides, draw_length, angle_subtend_deg)

arc(bob, 10, 30)

radius = 50
angle = 90
no_sides = 1

move_turtle (bob, no_sides, radius, angle)
circle(bob, radius)
pu(bob)
rt(bob, angle)
fd(bob, radius)
rt(bob, angle)
rt(bob, angle)


wait_for_user()					
