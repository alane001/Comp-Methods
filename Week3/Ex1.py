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


for i in range(points):
	y = spacing * i
	for j in range(points):
		x = spacing * j
		r1 = sqrt((x - x1)**2 + (y - y1)**2)
		r2 = sqrt((x - x2)**2 + (y - y2)**2)
		if r1 != 0 and r2 != 0:
			sqPlane[i, j] = phi(q1, r1) + phi (q2, r2)
#This fills up the plane for the potential

#This plots the potential in an image that shows its distribution
ax = plt.subplot(1,1,1)
imshow(sqPlane, origin = "lower", extent = [0, side, 0, side])
ax.set_xlabel('X Postion[cm]')
ax.set_ylabel('Y Postion[cm]')
plt.suptitle('Electrical Potential Distribution Due to Two Charges')
#gray()
show()

#I couldn't figure out how to do it by partial derivatives, so I just used the intrensic numpy function that does gradient
#This gives E = -gradient(voltage), the negative of sqplane makes it negative
grad = np.gradient(-sqPlane)
#The gradient gives two seperate arrays, with one for x and one for y

#Since the gradient is d/dx + d/dy then just add them together
#The abs gives that magnitude of the electric field
#grad[0] gives y and grad[1] gives x
eField = abs(grad[0] + grad[1])

#This plots the E field as a density plot
ax = plt.subplot(1,1,1)
imshow(eField, origin = "lower", extent = [0, side, 0, side])
ax.set_xlabel('X Postion[cm]')
ax.set_ylabel('Y Postion[cm]')
plt.suptitle('Electric Field Distribution Due to Two Charges')
#gray()
show()

#Shows off diaganol efield because when adding x and y causes a diaganol vector
