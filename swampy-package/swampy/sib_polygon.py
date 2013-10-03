# Polygon excercise from Week 0

# Name:

from TurtleWorld import * 		

world = TurtleWorld()			
bob = Turtle()				



# This is where you put code to move bob

import math 

def square (t, l):
	for i in range (4):
		fd (t, l)
		rt (t)

square (bob, 30)

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
	''' relates the number of sides and the length 
	of those sides to the circumference of the 
	circle with a given radius '''
	circumference = 2 * math.pi * r
	n = int (circumference / 3)
	l = circumference / n 
	polygon (t, l, n)

#circle (bob, 35)


def arc (t, r, theta):
 	arc_length = 2 * math.pi * r * theta / 360
	n = int (arc_length / 3)
	l = arc_length / n
	a = int (theta / n)
	square_ref (t, l, n, a)

	# making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    #lt(t, step_angle/2)
    #polyline(t, n, step_length, step_angle)
    #rt(t, step_angle/2)


arc (bob, 50, 30)

def circle_ref (t, r):
	arc (t, r, 360)

circle_ref()



wait_for_user()					
