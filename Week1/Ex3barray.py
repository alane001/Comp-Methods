import math as math
import numpy as np
import matplotlib.pyplot as plt

# Equation used: y=-1/2(9.81)t**2-vt+800 where y = 0, both negative because throwing down

# Known constants
grav = 9.81 # acceleration due to gravity in m/(s**2)
height = 800. # height of tower in meters

#Input min/max velocites
minVelocity = input('\nEnter the minimum velocity of the ball [m/s]: ')
maxVelocity = input('\nEnter the maximum velocity of the ball [m/s]: ')

#range of values, 10 bins
difference = float(maxVelocity) - float(minVelocity)  #forces float numbers, without causes error
spacing = difference / 10.  #this gives the amount of spacing between the 10 bins, equally spaced

#print ('\nThe spacing should be', spacing) #DELETE

#This will generate a list of velocities 
list_Velocities = []
i=0
startVel = minVelocity
while i <= 10:  #this gives full range between min/max, must have less than equal to
	list_Velocities.append(float(startVel))
	startVel = float(startVel) + float(spacing)
	i = i + 1
#print ('\nHere is the list of velocities:', list_Velocities) # DELETE

#Generate a list of times to go with velocities
j=0
list_times = []
while j <= 10:
	#Math inside squareroot of quadtratic equation
	insideSqrt = (math.pow(float(list_Velocities[j]), 2)) - (4.*(-(1./2.)*grav)*height)

	#Can't do +/- so this is the two parts of the quadratic equation
	#took negative out of -float(velocity) because want velocity going down, not up
	time1 = ((float(list_Velocities[j])) + math.sqrt(insideSqrt)) / (2. * (-(1./2.)*grav))
	time2 = ((float(list_Velocities[j])) - math.sqrt(insideSqrt)) / (2. * (-(1./2.)*grav))

	#Only output time if it is a postive value
	if time1 > 0:
		#print ('\nTime for ball to reach the ground:', time1, 'second(s)')
		list_times.append(float(time1))
	if time2 > 0:
		#print ('\nTime for ball to reach the ground:', time2, 'second(s)')
		list_times.append(float(time2))
	j = j + 1
#print ('\nHere is the list of times: ', list_times) # DELETE

#converting from list to an array for plotting
arrayvelo = np.array(list_Velocities)
arraytime = np.array(list_times)

#writing to a file with an array
np.savetxt('List of Times (array).ascii', arraytime, newline = '\r\n')

#plotting using an array
plt.plot(arrayvelo, arraytime, color='blue')
plt.xlabel('Initial Velocity [m/s]')
plt.ylabel('Time [s]')
plt.suptitle('Time Versus Initial Velocity of Ball')
plt.savefig('array time vs vel.png', format= 'png')
#plt.show()



