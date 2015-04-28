import numpy as np
import matplotlib.pylab as plt

def P(x):
	return 924 * x**6 - 2772 * x**5 + 3150 * x**4 - 1680 * x**3 + 420 * x**2- 42 * x + 1

#This gives the spacing, starting with (xmin, xmax, num of bins)
x = np.linspace(0, 1, 250)

#Gives y values
y = P(x)

#This is just so can plot a line where x = 0
xx = ([0,0])

#This will plot the function as red
plt.plot(x, y, 'r')
#This will plot the x = 0 line
plt.plot(xx, 'b')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.suptitle('Sixth Order Polynomial as a Function of X')

#This will save the figure as a png file
plt.savefig('Sixth Order Poly.png', format = 'png')
#plt.show()

#Now can inspect for roots, BY EYE
#Roots at: 0.03     .17        0.39       0.62       0.84     0.97

#Find all six roots using newtons method
#For newtons method we need the derivative of P(x) by hand

# P'(x) = 5544 * x**5 - 13860 * x**4 + 12600 * x**3 - 5040 * x**2 + 840 * x - 42

def P_prime(x):
	return  5544 * x**5 - 13860 * x**4 + 12600 * x**3 - 5040 * x**2 + 840 * x - 42

#Newtons Method: xnew = xguess - (f(xguess) / f'(xguess))

def newtMeth(x_old):
	#Error to force into while loop
	eps = 1.

	while eps > 1.e-10:
		x_new = x_old - (P(x_old) / P_prime(x_old))
		#print('x new =', x_new)
		#See p. 271 for this formula
		eps = abs(x_old - x_new)
		x_old = x_new
	return x_new

#Now can just plug in estimates from the graph into the function
print('First Root:', newtMeth(0.03), '\nSecond Root:', newtMeth(0.17), '\nThird Root:', newtMeth(0.39), '\nFourth Root:', newtMeth(0.62), '\nFifth Root:', newtMeth(0.84), '\nSixth Root:', newtMeth(0.97))


