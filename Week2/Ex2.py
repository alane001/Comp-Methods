import Ex1 as Ex1
import numpy as np
import matplotlib.pyplot as plt

#Loading given txt into an array
velArray = np.loadtxt("velocities.txt", float)

#This creats a list of just the times
listTime = []
j=0
while j < velArray.shape[0]:
	listTime.append(velArray[j, 0])
	j += 1
#This changes the list into an array
arrayTime = np.array(listTime)

#This creates a list of just the velocities
listVel=[]
k=0
while k < velArray.shape[0]:
	listVel.append(velArray[k, 1])
	k += 1
#This changes the list into an array
arrayVel = np.array(listVel)

#empty array to start
listPos = []
i=0
x=0
#loop to fill up list with x positions from velocities
while i < arrayTime.shape[0]:
	#call trapezoidal rule from previous program I created
	x = Ex1.trapez(arrayTime[i], arrayVel[i])
	listPos.append(x)
	i += 1

#converting list to array for plotting and saving
arrayPos = np.array(listPos)
print(arrayPos)
#saves as txt file
np.savetxt('List of Positions Trapez.txt', arrayPos, newline = '\r\n')

#Plotting two graphs on same output, one of the original array of velocity vs time and the other of position vs. time
ax = plt.subplot(2,1,1)
plt.plot(arrayPos, color='red')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.suptitle('Time Versus Position and Velocity')
ax2 = plt.subplot(2,1,2)
plt.plot(velArray, color = 'blue')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.show()

# Now for simposons rule

listVelSimp = []
#m=0
#y=0
#while m < velArray.shape[0]:
y = Ex1.simpson(arrayTime, arrayVel)
#	print(y)
listVelSimp.append(y)
#	m += 1

#change to array
arrayPosSimp = np.array(listVelSimp)

print(arrayPosSimp)
#saves output of array for position of simpsons rule
np.savetxt('List of Positions Simp.txt', arrayPosSimp, newline='\r\n')

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
