# Polygon excercise from Week 0

# Name:

from TurtleWorld import * 		

world = TurtleWorld()			
bob = Turtle()				



# This is where you put code to move bob

import math 

def square (t, l, n):
	for i in range (4):
		fd (t, l)
		rt (t)

square (bob, 10, 90)

def polygon (t, l, n): 
	angle = 360/n
	for i in range (n):
		fd (t, l)
		rt (t, angle)

polygon (bob, 10, 8)

def circle (t, r):
	circumference = 2 * math.pi * r
	n = 50
	l = circumference / n 
	polygon (t, l, n)

circle (bob, 50)




wait_for_user()					
