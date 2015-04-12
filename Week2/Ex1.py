import numpy as np

#This is for a general integration, the function must be calculated before putting it through this subroutine. These functions take in two arrays, on as the x value and one as the y value from the input of x into the y function

#Trapezoidal rule
def trapez(x, y):
	# Trapezoid equation: I = h [0.5*f(a) + 0.5*f(b) + (sum of all f(a+kh))]

	# I is integral, this is first part of integral, 1/2f(a) + 1/2f(b)
	#f(a) and f(b) correspond to the first(a) and last(b) of the y array
	#y.shape0 -1 gives the last value in the y array
	
	# h is the distance between the x array values
	h = (x[1] - x[0])

	#This just sums up the values of array y from second value (1) to final value
	S = np.sum(y[1:y.shape[0]-1])

	#Full integral
	I = (0.5*y[0] + 0.5*y[y.shape[0]-1] + S)
	
	# Last part to to multiply by outside h
	I = h * I
	return I

#The simpson's rule

def simpson(x, y):
	# The simpson equation: I = (1/3)*h [f(a) + f(b) + (4 * (sum of odd f(a+kh))) + (2 * (sum of even f(a+kh)))]

	#Slice width, difference between x arrays
	h = x[1] - x[0]

	# 1st part of equation, 1st and last of y array
	I1 = y[0] + y[y.shape[0]-1]
	
	#Sum up odd numbers, 1 start, up to N, by values of 2 (1,3,5) etc
	#keeps I1 separate so can multiply by 4
	# N = y.shape[0]-1 for book example
	I2 = 0.0
	for k in range(1, y.shape[0]-1, 2):
		I2+= y[k]
	I2 = I2 * 4
	
	#Sum up even numbers
	I3 = 0.0
	for j in range(2, y.shape[0]-1, 2):
		I3 += y[j]	
	I3 = I3 * 2
	
	#makes full integral
	I = I1 + I2 + I3

	# finishes up equation
	I = (I * h) / 3.
	return I

