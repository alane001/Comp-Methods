import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from cmath import exp

#My function for descrite fourier transform
#passing in y as an array
def dft(y):
	N = len(y)
	#complex, the N//2 gives on the integer, not any decimal
	c = np.zeros(N//2 +1, complex)

	for k in range (N//2+1):
		for n in range(N):
			#This fills in the constants, j is for (i) complex
			c[k] += y[n]*exp(-2j*np.pi*k*n/N)
	return c

#Wants N = 1000 evenly spaced points
t = np.linspace(0., 1., 1000)
#This generates a square wave info for one cycle
square = signal.square(2. * np. pi * t)

#This plotted the square wave to make sure it was only one cycle
#plt.plot(t, signal.square(2 *np.pi * t))
#plt.ylim(-2, 2)
#plt.xlim(-1, 2)
#plt.show()

#This plugs in the square waves values into the descrite fouier transform to find the coefficients
coeff = dft(square)

#This plots what we require
plt.plot(np.arange(len(coeff)), np.abs(coeff)**2)
plt.xlabel('Frequency (k)')
plt.ylabel('Absolute Val of Fourier Coeff')
plt.title('Fourier Coefficients vs. Frequency of Square Wave (1 Cycle)')
#This is to better see the high counts near 1
plt.xlim(-2, 100)
plt.show()


#PART B
#Sawtooth wave yn = n

sawtooth = signal.sawtooth(2. * np.pi * t)
coeffsaw = dft(sawtooth)
plt.plot(np.arange(len(coeffsaw)), np.abs(coeffsaw)**2)
plt.xlabel('Frequency (k)')
plt.ylabel('Absolute Val of Fourier Coeff')
plt.title('Fourier Coefficients vs. Frequency of Sawtooth Wave (1 Cycle)')
plt.xlim(-2, 100)
plt.show()


#PART C
#The modulated sine wave yn = sin(pi*n/N) * sin(20*pi*n/N)
N = 1000.
#This generates the n for the y calculation
n = np.arange(0, 1001, 1)
#did have n instead of t before, but wrong I believe
y = np.sin((np.pi * t) / N) * np.sin((20. * np.pi * t) / N)

coeffsin = dft(y)
plt.plot(np.arange(len(coeffsin)), np.abs(coeffsin)**2)
plt.xlabel('Frequency (k)')
plt.ylabel('Absolute Val of Fourier Coeff')
plt.title('Fourier Coefficients vs. Frequency of Modulated Sine Wave')
plt.xlim(-2, 100)
plt.show()

