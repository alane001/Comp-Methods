import numpy as np
from math import sqrt
import matplotlib.pylab as plt

### Cometary Orbits ###

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
	#print(fvx, fvy)
	return np.array([fx,fvx,fy,fvy],float)

#Time, dont use too high of a value for b or else causes odd orbit paths
a = 0.0 #intial time
b = 3e10 #final time

#Make sure to have N large enough, without it causes wierd things to happen
#How many bins/steps, the more steps the smoother the curve in the graph
N = 1000000

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
	
#print(xpoints)
#print(np.min(xpoints), np.max(xpoints), np.min(ypoints), np.max(ypoints))
plt.plot(xpoints, ypoints)
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.title("Position of the Comet")
plt.savefig("Position of the Comet.png", format = "png")
#plt.show()
