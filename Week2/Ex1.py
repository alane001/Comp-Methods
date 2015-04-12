import numpy as np

# Do we actually import an equation, f, and N instead of just (x,y) like shown in class? Also, is there an easier way to import an equation into the function other than lambda x:(equation), like seen at the bottom of the function?

def trapez(x, y, N, f):
	# Trapezoid equation: I = h [0.5*f(a) + 0.5*f(b) + (sum of all f(a+kh))]

	# Each slice width
	h = (y - x) / N
	
	#Ok I fixed the array part here above, i had float(y-x) which wouldnt allow the array to function


	# I is integral, this is first part of integral, 1/2f(a) + 1/2f(b)
	I = 0.5*f(x) + 0.5*f(y)
	
	# Runs through k slice of trapezoids, sum from k =1 to N, f(a+kh)
	for k in range(1, N):
		I += f(x+k*h)
	
	# Last part to to multiply by outside h
	I = h * I
	return I

x = np.array([0., -2])
y = np.array([2, 2])
q = trapez(x, y, 10, lambda x: (x**4-2*x+1))
print('This is the integral: ', q)

#THIS DOESNT WORK ABOVE ^ (now this works, ignore****)

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

t = simpson(0.0, 2.0, 10, lambda x: (x**4-2*x+1))
print('Integral for simpson: ', t)

