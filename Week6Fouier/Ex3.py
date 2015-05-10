import numpy as np
import matplotlib.pyplot as plt
from cmath import exp

#PART A

#Uploads the file for sunspots
sunspot = np.loadtxt('sunspots.txt', float)

#Isolates months, from 0 to 3142
month = sunspot[:, 0]

#Isolates Sun Spot Numbers
sunSpotNum = sunspot[:, 1]

#Plots the sunspot cycle
plt.plot(month, sunSpotNum, color = 'Blue')
plt.suptitle('Sunspot Cycle')
plt.xlabel('Month Number From Year 1749')
plt.ylabel('Sunspot Count')

#Use these to estimate the sunspot cycle, plots verticle lines
#plt.axvline(x = 75, color = 'k')
#plt.axvline(x = 210, color = 'k')

#Looks like they go in cycles of 135 months = 11.25 years

#This sets the x and y scales
#x from 0 to 3150 and y from 0 to 27
plt.axis([0, 3150, 0, 275])
plt.savefig('Sunspot Count as a Function of Time.png', format = 'png')
plt.show()

print('\nLooks like the sunspot cycle occurs in increments of 135 months or 11.25 years')

#PART B

#Function for descrite fouier transform from Ex2.py from week 5
def dft(y):
	N = len(y)
	#complex, the N//2 gives on the integer, not any decimal
	c = np.zeros(N//2 +1, complex)

	for k in range (N//2+1):
		for n in range(N):
			#This fills in the constants, j is for (i) complex
			c[k] += y[n]*exp(-2j*np.pi*k*n/N)
	return c

#This gives the coefficients of fourier transform
coeff = dft(sunSpotNum)

#This will plot a verticle line where needed to estimate other large frequency, 'k' is black
#plt.axvline(x = 24, color = 'k')

#Looks like the other main frequency is at k = 24

#This plots magnitude of Fouier Coeff
plt.plot(np.arange(len(coeff)), np.abs(coeff)**2)
plt.xlabel('Frequency (k)')
plt.ylabel('Absolute Val of Fourier Coeff')
plt.title('Fourier Coefficients vs. Frequency for Sunspot Cycle')
#This is to better see the high counts near 1, without, it blends
plt.xlim(-1, 100)
plt.ylim(0, 2.7e10)
plt.savefig('Fouier for Sunspot Cycle.png', format='png')
plt.show()


#PART C

#The only other non-zero k term is at k = 24 1/month
print("\nOther non-zero frequency at k = 24 as seen on the graph")

#To find period we need T = 1 / freq = 1/k but that would give 0.041 months which does not correspond to the answer in part A. Any value of k would give a low number so I am assuming we must multiply to somthing else

#To find the period of this k just multiply it by 2 pi
print("\nThe period of this sine wave is", 2. * np.pi * 24., "which is very close to the estimate 135 months, as predicted by part a.")



