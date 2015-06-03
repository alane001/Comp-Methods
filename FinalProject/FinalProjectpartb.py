import numpy as np
from math import sqrt
import matplotlib.pylab as plt

### Cometary Orbits ###

#PART A) is included in the function f(r)


#Part B) equal step size

#Constants
G = 6.6738e-11 # m**3 kg**-1 s**-2         Gravitational Constant
M = 1.9891e30 # kg      Mass of the Sun

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
#For two orbits we use 3.1e9
a = 0.0 #intial time
b = 3.1e9 #final time

#This b time gives almost exactly 2 orbital periods


#Make sure to have N large enough, without it causes wierd things to happen
#How many bins/steps, the more steps the smoother the curve in the graph
N = 1000000

#Do not make N smaller than this or else causes linear plots instead of orbital

#Step size
h = (b-a)/N

tpoints = np.arange(a,b,h)
xpoints = np.zeros(N)
ypoints = np.zeros(N)

# Initial Conditions

# r = (x,s,y,u) where s is velocity x and u is velocity y
# Converted to m from km
r = np.array([4e12, 0, 0, 500],float)

# Fourth order Runge-Kutta Method for ODE's
for i in range(N):
	t = tpoints[i]
	xpoints[i] = r[0]
	ypoints[i] = r[2]
	k1 = h*f(r)
	k2 = h*f(r+0.5*k1) 
	k3 = h*f(r+0.5*k2)
	k4 = h*f(r+k3)
	r += (k1+2*k2+2*k3+k4)/6
	

plt.figure(1)
plt.plot(xpoints, ypoints)
#postion of the sun in the orbit
plt.plot(0.3e12, 0., '-o', color = 'y')
plt.xlabel("X Position [m]")
plt.ylabel("Y Position [m]")
plt.title("Position of the Comet Using Equal Step Size - Two Orbits")
plt.tight_layout()
plt.savefig("Position of the Comet Part B.png", format = "png")
plt.show()

#array of zeros to get y =0 line to plot
zero = np.zeros(N)

plt.subplot(2,1,1)

#plots a y = 0 line
plt.plot(tpoints, zero, 'black')

plt.plot(tpoints, xpoints)
plt.xlabel("Time [s]")
plt.ylabel("X Position [m]")
plt.title("X Position of the Comet vs Time - Two Orbits")
plt.tight_layout() #makes the graph fit in frame without overlapping

plt.subplot(2,1,2)
plt.plot(tpoints, zero, 'black')
plt.plot(tpoints, ypoints)
plt.xlabel("Time [s]")
plt.ylabel("Y Position [m]")
plt.title("Y Position of the Comet vs Time - Two Orbits")
plt.tight_layout()
plt.savefig("X and Y Position of the Comet vs Time Part B.png", format = "png")
plt.show()


#The same step size causes the program to run slow compared to the adaptive step method. I used a h value of around 3100 secs, if N went smaller then that number would be larger and cause problems.
