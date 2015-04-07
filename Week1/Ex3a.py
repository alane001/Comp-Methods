import math as math

# Equation used: y=-1/2(9.81)t**2-vt+800 where y = 0, both negative because throwing down

# Known constants
grav = 9.81 # acceleration due to gravity in m/(s**2)
height = 800. # height of tower in meters

#Input intitial velocites
velocity = input('\nEnter the initial velocity of the ball [m/s]: ')

#Math inside squareroot of quadtratic equation
insideSqrt = (math.pow(float(velocity), 2)) - (4.*(-(1./2.)*grav)*height)

#Can't do +/- so this is the two parts of the quadratic equation
#took negative out of -float(velocity) because want velocity going down, not up
time1 = ((float(velocity)) + math.sqrt(insideSqrt)) / (2. * (-(1./2.)*grav))
time2 = ((float(velocity)) - math.sqrt(insideSqrt)) / (2. * (-(1./2.)*grav))

#Only output time if it is a postive value
if time1 > 0:
	print ('\nTime for ball to reach the ground:', time1, 'second(s)')
if time2 > 0:
	print ('\nTime for ball to reach the ground:', time2, 'second(s)')
