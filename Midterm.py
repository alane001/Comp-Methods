import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import newton

def f(t):
	return 100. * (np.sin(2.*np.pi*t) * t**2)

N = 50
spacing = 1. / 50.

#now this is the spacing for time interval of 50 bins
time = np.linspace(0, 1, 50)

#now have velocities at these times
vel = f(time)


#Plotting
plt.scatter(time, vel, color = 'blue')
plt.xlabel('Time (seconds)')
plt.ylabel('Velocity (m/s)')
plt.title("Velocity vs Time")
plt.show()

#save the velocities
np.savetxt("Velocities.acsii", vel, newline = "\r\n")

#Average velocity
aveVel = np.sum(abs(vel)) / float(N)
print("Average velocity of the particle:", aveVel, "m/s")

#Trapez rule
# 1/2fa + 1/2 fb
def trap(x, y):
	h = x[1] - x[0]
	
	#last value fb
	I1 = 1. / 2. * y[y.shape[0]-1]
	
	#first value fa
	I2 = 1. / 2. * y[0]

	I3 = np.sum(y[1:y.shape[0]-1])

	I = I1 + I2 + I3
	
	I = I * h
	return I

mytrapanswer = trap(time, vel)
print("My trap answer:", mytrapanswer)

knownint = np.trapz(vel, x = time)
print("Numpys answer:", knownint)


#Error for trap = 1/3 I2 - I1

N1=5
time1 = np.linspace(0, 1, N1)
vel1 = f(time1)
knownint1 = np.trapz(vel1, x=time1)


required = 1*10**(-6)
error = 10.
N2 = 10
# loop for error
while error > required:
	time2 = np.linspace(0, 1, N2)
	vel2 = f(time2)
	knownint2 = np.trapz(vel2, x = time2)
	
	# error = 1/3 * (I2-I1)
	error = 1. / 3. * (knownint2 - knownint1)
	
	knownint1 = knownint2
	N2 = N2 * 2


print("Smallest number of points:", N2)
	
#Can look at graph to see where it crosses the x axis
#print(newton(vel, 0.2))
