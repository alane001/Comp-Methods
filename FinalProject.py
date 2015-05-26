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

#def fx(r, v, t):
#	x = r[0]
#	y = r[1]
#	s = v[0]
#	fx = s
#	fs = -G * M * (x / ((x**2 + y**2)**(3/2)))
#	return np.array([fx, fs],float)


#def fy(r, v, t):
#	x = r[0]
#	y = r[1]
#	u = v[1]
#	fy = u
#	fu = -G * M * (y / ((x**2 + y**2)**(3/2)))
#	return np.array([fy, fu],float)

#IF USING r1 and r2
def fx(r,t):
	x = r[0]
	y = r[1]
	v = r[2]
	fx = v
	fv = -G * M * (x / ((x**2 + y**2)**(3/2)))
	return np.array([fx,fv], float)

def fy(r,t):
	x = r[0]
	y = r[1]
	v = r[2]
	fy = v
	fv = -G * M * (y / ((x**2 + y**2)**(3/2)))
	return np.array([fy,fv],float)



def f(r):
	x = r[0]
	vx = r[1]
	y = r[2]
	vy = r[3]
	fx = vx
	fy = vy
	#fv = -G * M * (sqrt((x-4e9)**2 + (y - 0)**2) / ((x**2 + y**2)**(3/2)))
	fvx = -G * M * (x / ((x**2 + y**2)**(3/2)))
	fvy = -G * M * (y / ((x**2 + y**2)**(3/2)))
	print(fvx, fvy)
	return np.array([fvx,fx,fvy,fy],float)

#This is time
a = 0.0 #intial time
b = 1e9 #final time

#How many bins/steps
N = 10

#Step size
h = (b-a)/N

tpoints = np.arange(a,b,h)
xpoints = np.zeros(N)
ypoints = np.zeros(N)

# Initial Conditions   [x , y]
#ro = np.array([4e9,0], float)   #initial postions in km   MIGHT HAVE TO CHANGE
#vo = np.array([0,500],float)    #initial velocities in m/s

#OR can change r into r(xo, yo, vo) where it is a function of position and velocity
#r1 = np.array([4e9, 0, 0],float)
#r2 = np.array([4e9, 0, 500],float)

# r = (x,s,y,u) where s is velocity x and u is velocity y
# Converted to m from km
r = np.array([4e12, 0, 0, 500],float)

# Fourth order Runge-Kutta Method for ODE's
for i in range(N): 
    t = tpoints[i]
    xpoints[i] = r[0]
    ypoints[i] = r[2]
    k1 = h*f(r)#)
    k2 = h*f(r+0.5*k1)#,t+0.5*h)
    k3 = h*f(r+0.5*k2)#,t+0.5*h)
    k4 = h*f(r+k3)#,t+h)
    r += (k1+2*k2+2*k3+k4)/6

print(np.min(xpoints), np.max(xpoints), np.min(ypoints), np.max(ypoints))
plt.plot(xpoints, ypoints)
plt.show()
