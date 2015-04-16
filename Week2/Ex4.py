import Ex1 as Ex1
import numpy as np
import math as m

#Required function, leave as radians
def f(x):
	return ((np.sin(np.sqrt(100.*x)))**2)

#This is the error we want to obtain
necessaryError = float(1*10**(-6))

#This is the integrals limits of integration
a = 0.
b = 1.

#This is the number of bins
N = 1

#To get it to go into the loop
errorTrap = 1

#This makes sure that it doesnt do the error estimate for only a single value
integralTrapOld = 0

#Keeps looping until the calculate error is under the necessary error
while errorTrap > necessaryError:
	
	#This gives the spacing between the bins
	h = (b - a) / N

	#Makes an array of zeros to be filled in later
	xValue = np.zeros(N+1)

	#This next part fills in the x array with the proper values and spacing
	start = 0.
	
	for i in range(N+1):
		#Allows for putting 0 in as the first value of the array
		if i == 0:
			xValue[i] = a
		else:
			xValue[i] = start + h
			start += h
		i += 1

	#This gives an array of y(x) values to passed into my function
	yValue = f(xValue)
	
	#Now can pass these x and y arrays into my trapez and simpson functions
	integralTrap = Ex1.trapez(xValue, yValue)
	
	print("\nN:", N)
	print("Integral Trap:", integralTrap)
	
	if integralTrapOld != 0:
		#Calculation of error
		errorTrap = abs((1./3.)*(integralTrap - integralTrapOld))
		print("Error Trap:", errorTrap)
	else:
		#Print this value for the first N since it can't calculate error with a single integrated value
		print("Error Trap:", 0.)
	
	integralTrapOld = integralTrap
	
	#Causes N to double, this allows for I2 to be calculated
	N = N * 2

print("\nDONE")
