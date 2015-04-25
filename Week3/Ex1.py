import numpy as np
import matplotlib.pyplot as plt
from pylab import imshow,gray,show
from math import sqrt

#Calculating Electric Field of charges

#Mathematical Pi
pi = 3.14159

#Electric constant
epsilonKnot =  8.854187817 #units of C2/(N m2) 

#Electric potential (phi)
#Where q is the charge and r is the distance from the charge
def phi(q, r):
	return q / (4. * pi * epsilonKnot * r)


def partx(func, x, y, h):
	dx = (func(x + h / 2., y) - func(x - h / 2., y)) / h
	return dx

def party(func, x, y, h):
	dy = (func(x, y + h / 2.) - func(x, y - h / 2.)) / h
	return dy

#Charges used
q1 = 1. #unit of C
q2 = -1. #unit of C

#Potentials will add by superposition, 2 charges are spaced apart by 10 cm
#I will put these charges at postion (45,45) and (55,45)

#r1 = sqrt((x-x1)^2 + (y-y1)^2) etc...
separation = 10.0 #cm
side = 100.0
points = 500
spacing = side / points

#Calc positions of the centers of the charges
x1 = side / 2 + separation / 2
y1 = side / 2
x2 = side / 2 - separation / 2
y2 = side / 2

#Need to make a matrix of a 1m x 1m grid, broken into 1 cm increments
sqPlane = np.zeros(shape=(points, points)).astype('float')
ePlane = np.zeros(shape=(points, points)).astype('float')

h=1.
for i in range(points):
	y = spacing * i
	for j in range(points):
		x = spacing * j
		r1 = sqrt((x - x1)**2 + (y - y1)**2)
		r2 = sqrt((x - x2)**2 + (y - y2)**2)
		if r1 != 0 and r2 != 0:
			sqPlane[i, j] = abs(phi(q1, r1)) + abs(phi (q2, r2))
			
					
ax = plt.subplot(1,1,1)
imshow(sqPlane, origin = "lower", extent = [0, side, 0, side])
ax.set_xlabel('X Postion[cm]')
ax.set_ylabel('Y Postion[cm]')
plt.suptitle('Electrical Potential Distribution Due to Two Charges')
#gray()
show()

#Electric Field = -gradient(phi)
#eField = np.gradient()
#print(eField)

#Partial derivatives

#ePlane[i, j] = abs(partx(lambda q1,r1:phi(q1, r1), x, y, h) + party(phi(q1, r1), x, y, h) + partx(phi(q2, r2), x, y, h) + party(phi(q2, r2), x, y, h))
