#header

#script
from swampy.TurtleWorld import * 

world = TurtleWorld()
bob = Turtle ()
print bob 



def square (t, length):
	edge(t, length)
	edge(t, length)
	edge(t, length)
	edge(t, length)

def edge (t, length):
	fd (bob, length)
	rt(bob)


square(bob, 90)

square(bob, 110)

wait_for_user()



