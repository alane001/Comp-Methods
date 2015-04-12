import Ex1 as Ex1
import numpy as np
import matplotlib.pyplot as plt

#Loading given txt into an array
a = np.loadtxt("velocities.txt", float)

#empty array to start
listVel = []
i=0
x=0
#loop to fill up list with x positions from velocities
while i < a.shape[0] - 1:
	#call trapezoidal rule from previous created program I created
	x = Ex1.trapez(float(a[i, 0]), float(a[i+1, 0]), 10, lambda t: float(a[i, 1])*t+x)
	listVel.append(x)
	i += 1

#converting list to array for plotting and saving
arrayPos = np.array(listVel)
#saves as txt file
np.savetxt('List of positions.txt', arrayPos, newline = '\r\n')

#Plotting two graphs on same output, one of the original array of velocity vs time and the other of position vs. time
ax = plt.subplot(2,1,1)
plt.plot(arrayPos, color='red')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.suptitle('Time Versus Position and Velocity')
ax2 = plt.subplot(2,1,2)
plt.plot(a, color = 'blue')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.show()

# now for simposons rule

listVelSimp = []
j=0
y=0
while j < a.shape[0] - 1:
	#print(j)
	y = Ex1.simpson(float(a[j, 0]), float(a[j+1, 0]), 10, lambda x: float(a[j, 1])*x+y)
	#print(y)
	listVelSimp.append(y)
	j += 1

#change to array
arrayPosSimp = np.array(listVelSimp)

#saves output of array for position of simpsons rule
np.savetxt('List of Positions Simp.txt', listVelSimp, newline='\r\n')

#Graphs to compare the simpson's rule to trapezoidal rule

ax3 = plt.subplot(2,1,1)
plt.plot(arrayPos, color='red')
plt.xlabel('Time (s)')
plt.ylabel('Position of Trapezoid (m)')
plt.suptitle('Time Versus Position and Velocity')
ax4 = plt.subplot(2,1,2)
plt.plot(arrayPosSimp, color = 'blue')
plt.xlabel('Time (s)')
plt.ylabel('Position of Simpson (m)')
plt.show()
