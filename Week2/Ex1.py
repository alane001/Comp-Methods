import numpy as np

def trapez(x, y):
	# Trapezoid equation: I = h [0.5*f(a) + 0.5*f(b) + (sum of all f(a+kh))]

	# I is integral, this is first part of integral, 1/2f(a) + 1/2f(b)
	#f(a) and f(b) correspond to the first(a) and last(b) of the y array
	#y.shape0 -1 gives the last value in the y array
	I = 0.5*y[0] + 0.5*y[y.shape[0]-1]
	print('first I:', I)

	# Runs through k slice of trapezoids, sum from k =1 to N, f(a+kh)
	# h = to space betwen any two consective points in the x array
	#h = (x[x.shape[0]-1] - x[0]) / x.shape[0]
	h = (x[1] - x[0])
	print(y)
	for k in range(1, y.shape[0]-1):
		#this makes sure that the first and last values of y are not included
		I += y[k]
	
	# Last part to to multiply by outside h
	I = h * I
	return I

#From Prof. Sales to test function
def f(x):
	return x**4 - 2.*x + 1

a = 0.
b = 2.
N = 10

dx = (b - a) / float(N)
x = a + np.arange(N).astype('float') * dx + dx/2
y = f(x)
integral = trapez(x,y)    #here is where you define your trapez function
print('integral:', integral)
print('FINISHED')

#THIS WORKS BELOW
#q = trapez(0.0, 2.0, 10, lambda x: x**4-2*x+1)
#print('This is the integral: ', q)
#This gives 4.50 like from the example in the book



#The simpson's rule works as well now I believe


def simpson(x, y, N, f):
	# The simpson equation: I = (1/3)*h [f(a) + f(b) + (4 * (sum of odd f(a+kh))) + (2 * (sum of even f(a+kh)))]

	#Slice width
	h = (y - x) / N

	# 1st part of equation
	I1 = f(x) + f(y)
	
	#Sum up odd numbers, 1 start, up to N, by values of 2 (1,3,5) etc
	#keeps I1 separate so can multiply by 4
	I2 = 0.0
	for k in range(1, N, 2):
		I2+= f(x+k*h)
	I2 = I2 * 4
	
	#Sum up even numbers
	I3 = 0.0
	for j in range(2, N, 2):
		I3 += f(x+j*h)	
	I3 = I3 * 2
	
	#makes full integral
	I = I1 + I2 + I3

	# finishes up equation
	I = (I * h) / 3.
	return I

#t = simpson(0.0, 2.0, 10, lambda x: (x**4-2*x+1))
#print('Integral for simpson: ', t)

