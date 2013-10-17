# Flower excercise (4.2) from Week 0

# Name: Ceceilia Allwein



from TurtleWorld import * 	 
import math 

world = TurtleWorld()			
bob = Turtle()
bob.delay = 0.01				



# This is where you put code to move bob


# FUNCTIONS

def line_subtend (turtle, no_sides, seg_length, angle):
    '''  
    Moves and draws line segments + turns. 
    This is called polyline in the text 
    '''
    pd (turtle)
    for i in range (no_sides):
        pd (turtle)
        fd (turtle, seg_length)
        lt (turtle, angle)


def arc_mine (turtle, radius, angle):
    '''
    writes only a portion of the circumference 
    of a circle, with a given radius and 
    angle that the arc subtends 
    ''' 
    circumference = 2 * math.pi * radius
    seg_length = circumference * (angle / 360)
    no_sides = int(seg_length / radius)
    draw_length = float(seg_length / no_sides)
    angle_subtend_deg = angle / no_sides
    line_subtend (turtle, no_sides, seg_length, angle)
    rt(turtle, angle_subtend_deg/2)

def arc_duo (turtle, radius, angle):
	for i in range (2):
        arc_mine (turtle, radius, angle)
        lt (turtle, 180-angle)

# test call
# arc_duo (bob, 25, 45)


def flower (turtle, radius, no_petals, angle):
    for i in range (no_petals): 
        arc_duo (turtle, radius, angle)
        lt (turtle, 360/no_petals)

# test call
# flower(bob, 15, 8, 45)


def position (turtle, distance):
    pu (turtle)
    fd (turtle, distance)
    pd (turtle)



# CALLS

position(bob, -100)
flower(bob, 7, 60.0, 60.0)

position(bob, 100)
flower(bob, 10, 40.0, 80.0)

position(bob, 100)
flower(bob, 20, 140.0, 20.0)






# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.


if __name__ == '__main__':
    world = TurtleWorld()    

    bob = Turtle()
    bob.delay = 0.001

    # draw a circle centered on the origin
    radius = 100
    pu(bob)
    fd(bob, radius)
    lt(bob)
    pd(bob)
    arc(bob, radius, 35)

    wait_for_user()
				

