import numpy as np

#Linear Equations

#PART A EQUATIONS: where V+ = 5 volts

#Had a problem here that caused all the results to be 5 volts. This came from having 2V2 -V1-V4=0 instead of 3V2. This was because I didn't take into account the voltage compared with the ground giving v2 - 0(ground) / R. See p.220 of book.

# 4V1 - V2 - V3 - V4 = V+  Given in book
# 3V2 - V1 - V4 = 0
# 3V3 - V1 - V4 = V+
# 4V4 - V3 - V1 - V2 = 0

#Two are attached to ground, so zero volts

#This will look like:

# |4 -1 -1 -1| |V1|   |5|
# |-1 3  0 -1| |V2| = |0|
# |-1 0  3 -1| |V3|   |5|
# |-1 -1 -1 4| |V4|   |0|

#Had to move it around so that zero's didn't land in the diagonal portion or else would cause a divide by zero error.

#Turn this into an array, with form Ax = v
A = np.array([[4., -1., -1., -1.], [-1., 3., 0., -1.], [-1., 0., 3., -1.], [-1., -1., -1., 4.]])

v = np.array([5., 0., 5., 0.])

#Now for gaussian elimination

#This gives the length of the array v
N = len(v)

for i in range(N):
	#Dividing by diagonal elements (all at 0,0 | 1,1 | 2,2 | 3,3)
	#One run through divides entire row by element at 0,0 etc...
	div = A[i,i]
	#does this to entire row
	A[i, :] /= div
	v[i] /= div
	
	
	#Now subtract from the lower rows
	#The i+1 causes it to go to next row so that it can multi by that first rows value
	for j in range(i+1, N):
		mult = A[j, i]
		A[j,:] -= mult*A[i,:]
		v[j] -= mult*v[i]

#This(^) gives us an upper matrix (U), can print A to see

#Now for backsubstution

#This is the empty array for x in the Ax = v equation
x = np.zeros(N, 'float')

#range(Start, stop, steps) so it goes backwards this time
for i in range (N-1, -1, -1):
	x[i] = v[i]
	for j in range(i+1, N):
		x[i] -= A[i,j]*x[j] 
print("X vector for my function:", x)

#Now can compute with just numpy's intrinsic function for solving linear algebra
#Just plug in the two array corresponding to Ax = v and solves for x automatically. A is the coef. matrix, and v is the dependent variable values.
luMethod = np.linalg.solve(A, v)
print("Numpy's Linear Algebra Method:", luMethod)

#This will print if the two methods agree
if x.all() == luMethod.all():
	print("They match!\n")

print("Voltage at v1:", x[0], "\nVoltage at v2:", x[1], "\nVoltage at v3:", x[2], "\nVoltage at v4:", x[3])
