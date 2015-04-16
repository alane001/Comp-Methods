import Ex1 as Ex1
import numpy as np
import matplotlib.pyplot as plt

#Loading given txt into an array
velArray = np.loadtxt("velocities.txt", float)

#This creates an array of just the times
#The : means take all values
time = velArray[:,0]

#This creates an array of just the velocities
vel = velArray[:,1]

#len means length of that array
posTrap = np.zeros(len(time))
posSimp = np.zeros(len(time))
distTrap = np.zeros(len(time))
distSimp = np.zeros(len(time))

#First is trapezodial rule
#Must start at 2 in order for [0:2] means [0, 1]
i = 2
while i < len(time):
	posAtTrap = Ex1.trapez(time[0:i], vel[0:i])
	distAtTrap = Ex1.trapez(abs(vel[0:i]), time[0:i])
	posTrap[i] = posAtTrap
	distTrap[i] = distAtTrap
	i += 1

#Now for simpson's rule
i = 2
while i < len(time):
	posAtSimp = Ex1.simpson(time[0:i], vel[0:i])
	distAtSimp = Ex1.simpson(abs(vel[0:i]), time[0:i])
	posSimp[i] = posAtSimp
	distSimp[i] = distAtSimp
	i += 1

#This will sum up the distance array's of each to give a total distance
totalDisTrap = np.array([sum(distTrap)])
totalDisSimp = np.array([sum(distSimp)])

#These will save the files of total distances
np.savetxt('Total Distance Trap.txt', totalDisTrap)
np.savetxt('Total Distance Simp.txt', totalDisSimp)


#This plots the velocity vs time and position vs time on same figure
plt.subplot(2,1,1)
plt.plot(time, posTrap, color='red')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.suptitle('Time Versus Position and Velocity')
plt.subplot(2,1,2)
plt.plot(time, vel)
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.show()

