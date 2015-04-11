import numpy as np

def trapez(x, y, N, f):
	
	# Each slice width
	h = (y - x) / N
	
	#Ok I fixed the array part here above, i had float(y-x) which wouldnt allow th	e array to function


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
