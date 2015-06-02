import numpy as np
from math import sqrt
import matplotlib.pylab as plt

### Cometary Orbits with varying step size ###

#Part C)

#Constants
G = 6.6738e-11 # m**3 kg**-1 s**-2         Gravitational Constant
M = 1.9891e30 # kg      Mass of the Sun
delta = 3.16887e-5 #m per year # convert to seconds   given 1km/year need to convert to m/sec   1 year = 31556926 seconds

# Equations
# d^2 x/dt^2 = -GM x/r^3
# d^2 y/dt^2 = -GM y/r^3           where r = sqrt(x**2 + y**2)

def f(r):
	x = r[0]
	vx = r[1]
	y = r[2]
	vy = r[3]
	r = sqrt(x**2 + y**2)
	fx = vx
	fy = vy
	fvx = -G * M * (x / r**3) 
	fvy = -G * M * (y / r**3) 
	return np.array([fx,fvx,fy,fvy],float)

#Time, dont use too high of a value for b or else causes odd orbit paths
#1.6e9 seems to give one orbit
a = 0.0 #intial time
b = 1.6e9 #final time
tend = b

#Make sure to have N large enough, without it causes wierd things to happen
#How many bins/steps, the more steps the smoother the curve in the graph
#N = 1000000

N = 15000 #Guess the number of points since we will not know to begin with

#Step size
#h = (b-a) / N

#cant uses a know step value for t like before
tpoints = np.zeros(N)
xpoints = np.zeros(N)
ypoints = np.zeros(N)

# Initial Conditions

# r = (x,s,y,u) where s is velocity x and u is velocity y
# Converted to m from km
r = np.array([4e12, 0, 0, 500],float)

#array to keep h values
h_keep = np.zeros(N)
tnow = 0
nstep = 0 #allows for counting of steps
h = 20000000.  #initial guess of h

while tnow < tend:
	#print ('----- starting new step ----')
	#print ('time=,',tnow)
	#print ('step=, h=',(nstep,h))
	#print ('r=',r)

	redo = 0
	
	while redo != 1:
		#DO ANOTHER LOOP TO REDO EVERYTHING WHEN RHO IS LESS THAN ONE

		# Need x1 where start at time t and do two steps of size h
		r1 = r.copy()   #need a copy of orignal r
		
		#This will do 2 steps with bin h
		for istep in range(2):
			k1 = h*f(r1)
			k2 = h*f(r1+0.5*k1) 
			k3 = h*f(r1+0.5*k2)
			k4 = h*f(r1+k3)
			r1 += (k1+2*k2+2*k3+k4)/6
			if istep == 0:
				r1_1h = r1.copy()
		x1 = r1


		# Need x2 where we do a single large step of size 2h
		r3 = r.copy()
	
		
		k1 = 2*h*f(r3)
		k2 = 2*h*f(r3+0.5*k1) 
		k3 = 2*h*f(r3+0.5*k2)
		k4 = 2*h*f(r3+k3)
		r3 += (k1+2*k2+2*k3+k4)/6
	
		x2 = r3

		var = np.sqrt((x1[0]-x2[0])**2+(x1[2]-x2[2])**2)  #need to make decision on what to compare: error will be in coordinates x and y only 
		
		if var > 0:
			rho = (30. * h * delta) / var
		else:
			rho = 16.   #so new h = 2 *h
		
		#Now for rho to see if less than or greater than 1 

		#rho = (30. * h * delta) / abs(x1 - x2)

	
		if rho >= 1:
			#if larger than 2*h keep 2*h not larger
			newh = h * (rho)**(1./4.)
			
			if newh > 2.*h:
				newh = 2.*h

			#This makes it exit the loop
			redo = 1

			r = r1_1h
			tnow += h
			

			#keep quantities
			i = nstep
			xpoints[i] = r1_1h[0]
			ypoints[i] = r1_1h[2]
			tpoints[i] = h
			h_keep[i] = h

			#now use new h
			h = newh
			nstep += 1

		
		else:
			newh = h * (rho)**(1./4.)
		
			#redo with newh as the new h value for loop
			h = newh
			#makes the loop repeat
			redo = 0
			#print( 'FAILED, RE-DOING STEP')

	

# re-shape arrays with needed number of elements
tpoints = tpoints[0:nstep]
xpoints = xpoints[0:nstep]
ypoints = ypoints[0:nstep]
h_keep = h_keep[0:nstep]


	

plt.figure(1)

#This makes the graph print dots at each R-K step
for i in range(nstep):
	plt.plot(xpoints[i], ypoints[i], '-o')
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.title("Position of the Comet")
plt.savefig("Position of the Comet Adaptive.png", format = "png")
plt.show()

#array of zeros to get y =0 line to plot
zero = np.zeros(nstep)

plt.subplot(2,1,1)

#plots a y = 0 line
plt.plot(tpoints, zero, 'black')

plt.plot(tpoints, xpoints)
plt.xlabel("Time (s)")
plt.ylabel("X Position (m)")
plt.title("X Position of the Comet vs Time")
plt.tight_layout() #makes the graph fit in frame without overlapping

plt.subplot(2,1,2)
plt.plot(tpoints, zero, 'black')
plt.plot(tpoints, ypoints)
plt.xlabel("Time (s)")
plt.ylabel("Y Position (m)")
plt.title("Y Position of the Comet vs Time")
plt.tight_layout()
plt.savefig("X and Y Position of the Comet vs Time for Adaptive Steps.png", format = "png")
plt.show()

# plot orbit as a function of time
#dist = np.sqrt(xpoints**2 + ypoints**2)
#plt.figure(2)
#plt.plot(tpoints,dist,'--',linewidth=3)
#plt.title("Orbit as a Function of Time")
#plt.xlabel('Time [sec]')
#plt.ylabel('Distance [m]')

# plot step size
#plt.figure(3)
#ax1 = plt.subplot(111)
#plt.plot(tpoints,h_keep,'-',linewidth=2)
#ax1.set_yscale('log')
#plt.title("Step size vs Time")
#plt.xlabel("Time [sec]")
#plt.ylabel("Log of Step Size")
#plt.show()
