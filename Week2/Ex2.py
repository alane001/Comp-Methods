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

#Now break these into 10 chunks
#first chunk
i = 0
set1time = []
set1vel = []
while i < 10:
	set1time.append(arrayTime[i])
	set1vel.append(arrayVel[i])
	i+=1
array1time = np.array(set1time)
array1vel = np.array(set1vel)

#second chunk
i = 10
set2time = []
set2vel = []
while i < 20:
	set2time.append(arrayTime[i])
	set2vel.append(arrayVel[i])
	i+=1
array2time = np.array(set2time)
array2vel = np.array(set2vel)

#third chunk
i = 20
set3time = []
set3vel = []
while i < 30:
	set3time.append(arrayTime[i])
	set3vel.append(arrayVel[i])
	i+=1
array3time = np.array(set3time)
array3vel = np.array(set3vel)

#fourth chunk
i = 30
set4time = []
set4vel = []
while i < 40:
	set4time.append(arrayTime[i])
	set4vel.append(arrayVel[i])
	i+=1
array4time = np.array(set4time)
array4vel = np.array(set4vel)

#fifth chunk
i = 40
set5time = []
set5vel = []
while i < 50:
	set5time.append(arrayTime[i])
	set5vel.append(arrayVel[i])
	i+=1
array5time = np.array(set5time)
array5vel = np.array(set5vel)

#sixth chunk
i = 50
set6time = []
set6vel = []
while i < 60:
	set6time.append(arrayTime[i])
	set6vel.append(arrayVel[i])
	i+=1
array6time = np.array(set6time)
array6vel = np.array(set6vel)

#seventh chunk
i = 60
set7time = []
set7vel = []
while i < 70:
	set7time.append(arrayTime[i])
	set7vel.append(arrayVel[i])
	i+=1
array7time = np.array(set7time)
array7vel = np.array(set7vel)

#eighth chunk
i = 70
set8time = []
set8vel = []
while i < 80:
	set8time.append(arrayTime[i])
	set8vel.append(arrayVel[i])
	i+=1
array8time = np.array(set8time)
array8vel = np.array(set8vel)

#ninth chunk
i = 80
set9time = []
set9vel = []
while i < 90:
	set9time.append(arrayTime[i])
	set9vel.append(arrayVel[i])
	i+=1
array9time = np.array(set9time)
array9vel = np.array(set9vel)

#tenth chunk
i = 90
set10time = []
set10vel = []
while i <= 100:
	set10time.append(arrayTime[i])
	set10vel.append(arrayVel[i])
	i+=1
array10time = np.array(set10time)
array10vel = np.array(set10vel)

#Now find the positions of these ten chunks
#First do trapezoidal rule
pos1 = Ex1.trapez(array1time, array1vel)
pos2 = Ex1.trapez(array2time, array2vel)
pos3 = Ex1.trapez(array3time, array3vel)
pos4 = Ex1.trapez(array4time, array4vel)
pos5 = Ex1.trapez(array5time, array5vel)
pos6 = Ex1.trapez(array6time, array6vel)
pos7 = Ex1.trapez(array7time, array7vel)
pos8 = Ex1.trapez(array8time, array8vel)
pos9 = Ex1.trapez(array9time, array9vel)
pos10 = Ex1.trapez(array10time, array10vel)

#Take the positions and subtract from eachother with their absolute values to get the total distance traveled
totalDisTrap = abs(pos2 - pos1) + abs(pos3 - pos2) + abs(pos4 - pos3) + abs(pos5 - pos4) + abs(pos6 - pos5) + abs(pos7 - pos6) + abs(pos8 - pos7) + abs(pos9 - pos8) + abs(pos10 - pos9)

#Turn this into an array to be able to save txt
totalDistanceTrap = np.array([totalDisTrap])

#saves total distance as a txt file
np.savetxt('Total Distance Traveled Trapez.txt', totalDistanceTrap)




#Now do it for simpson's rule
pos1s = Ex1.simpson(array1time, array1vel)
pos2s = Ex1.simpson(array2time, array2vel)
pos3s = Ex1.simpson(array3time, array3vel)
pos4s = Ex1.simpson(array4time, array4vel)
pos5s = Ex1.simpson(array5time, array5vel)
pos6s = Ex1.simpson(array6time, array6vel)
pos7s = Ex1.simpson(array7time, array7vel)
pos8s = Ex1.simpson(array8time, array8vel)
pos9s = Ex1.simpson(array9time, array9vel)
pos10s = Ex1.simpson(array10time, array10vel)

totalDisSimp = abs(pos2s - pos1s) + abs(pos3s - pos2s) + abs(pos4s - pos3s) + abs(pos5s - pos4s) + abs(pos6s - pos5s) + abs(pos7s - pos6s) + abs(pos8s - pos7s) + abs(pos9s - pos8s) + abs(pos10s - pos9s)

totalDistanceSimp = np.array([totalDisSimp])

#Now save as a txt file
np.savetxt('Total Distance Traveled Simpson.txt', totalDistanceSimp)




#Plotting two graphs on same output, one of the original array of velocity vs time and the other of position vs. time

#This sets up the data to plot
graphVel = np.array([0, pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10])
graphTime = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

ax = plt.subplot(2,1,1)
plt.plot(graphTime, graphVel, color='red')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.suptitle('Time Versus Position and Velocity')
ax2 = plt.subplot(2,1,2)
plt.plot(arrayTime, arrayVel, color = 'blue')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.show()
