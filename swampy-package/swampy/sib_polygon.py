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

def line_subtend (turtle, no_sides, seg_length, angle):
	''' draws line segments + turns similar
	to square or square_ref '''
	for i in range (no_sides):
		fd (turtle, seg_length)
		rt (turtle, angle)

def polygon (turtle, no_sides, seg_length): 
	''' determines the angle of the turn 
	based on the given number of sides'''
	angle = 360.0 / no_sides
	line_subtend (turtle, no_sides, seg_length, angle)

def arc (turtle, radius, angle):
	'''defines 
	''' 
	circumference = 2 * math.pi * radius
	seg_length = circumference * angle / 360
	no_sides = int(seg_length / radius)
	draw_length = float(seg_length / no_sides)
	angle_subtend_deg = angle / no_sides
	line_subtend (turtle, no_sides, draw_length, angle_subtend_deg)

arc(bob, 10, 30)

wait_for_user()					
