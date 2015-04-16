import numpy as np
import Ex1 as Ex1
import scipy as scipy
from scipy.integrate import simps

#Since my program takes in two arrays, must compute function before passing it to the trapez function
def f(x):
	return x**4-2*x+1

#This is the integrals limits of integration
a = 0.
b = 2.
#This is the number of bins
N = 20
#This gives the spacing between the bins
h = (b-a) / N

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
integralSimp = Ex1.simpson(xValue, yValue)

print("My Function's Integral Trap:", integralTrap, "\nMy Function's Integral Simp:", integralSimp)

#Now can do numpy's intrinsic trapz's and simpson's functions
#these functions go (y, x) instead of x,y in my function

#If want to use numpy instead of scipy, use this
#integralTrapNp = np.trapz(yValue, xValue)
#print('Integral Numpy Trap:', integralTrapNp)

integralTrapSci = scipy.trapz(yValue, xValue)
print('Integral Scipy Trap:', integralTrapSci)
#This was causing problems
integralSimpSci = simps(yValue, xValue)
print('Integral Scipy Simpson:', integralSimpSci)



#Now to compute the error later, by starting with N = 10

#This is the integrals limits of integration
a2 = 0.
b2 = 2.
#This is the number of bins
N2 = 10
#This gives the spacing between the bins
h2 = (b2-a2) / N2

#Makes an array of zeros to be filled in later
xValue2 = np.zeros(N2+1)
#This next part fills in the x array with the proper values and spacing
start2 = 0.
for i in range(N2+1):
	#Allows for putting 0 in as the first value of the array
	if i == 0:
		xValue2[i] = a2
	else:
		xValue2[i] = start2 + h2
		start2 += h2
	i += 1

#This gives an array of y(x) values to passed into my function
yValue2 = f(xValue2)

#Now can pass these x and y arrays into my trapez and simpson functions
integralTrap2 = Ex1.trapez(xValue2, yValue2)
integralSimp2 = Ex1.simpson(xValue2, yValue2)

#These are the I1 in the formula for error (E = 1/3(I2-I1))

#if want to print results from second integrals
#print("\nSecond integral trap:", integralTrap2, "\nSecond integral simp:", integralSimp2)

#Now we can use the result from part one and the part above to calculate the error in the trap and simp rules, I2(N=20) = integralTrap, I1(N=10) = integralTrap2
#All of these errors for my Ex1 functions
#N1 is from the second integrations because it is the smaller, N=10

# trap error 1/3 (I2-I1)
errorTrap = abs((1./3.)*(integralTrap - integralTrap2))
# simp error 1/15(I2-I1)
errorSimp = abs((1./15.)*(integralSimp - integralSimp2))

#To print errors
#print("Trapezoidal Error:", errorTrap, "\nSimpson Error:", errorSimp)



#The calulated by hand constant
calcHand = 4.4
print("\nThe calculated, true result by hand is", calcHand, "and the computer calculated results", integralTrap, "+/-", errorTrap, "trapezoidal rule, and", integralSimp, "+/-", errorSimp, "simpson's rule")
