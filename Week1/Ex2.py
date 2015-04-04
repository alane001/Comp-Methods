import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

#arrays for all of the scores for each student
Homework = np.array([10., 10., 8., 9.5, 3., 9., 0, 6.])   
Mid_term = np.array([10., 10., 10., 10., 8., 5., 10., 7.]) 
Final_Project = np.array([9., 10., 10., 6., 10., 6., 8., 9.])

# This calcualtes final grade and adds each grade to a list
i=0
Grade=0
list_Grades = []  #an empty list
while i < Homework.shape[0]:
	Grade = Homework[i]*0.4 + Mid_term[i]*0.2 + Final_Project[i]*0.4
	i=i+1
	list_Grades.append(Grade)  #adds grade value to empty list

# This is to get the program to write the list to a file
printFile = open('List of Grades.txt', 'w+')
printFile.write("\n".join(map(lambda x: str(x), list_Grades)))
#printFile.write("\n".join(str(x) for x in list_Grades))   Another way to do it
printFile.close()

# now to check how many failed
k=0
failCount = 0
while k < Homework.shape[0]:
	if list_Grades[k] < 6:
		failCount = failCount + 1
	k = k + 1
print ('\nNumber of students that failed:', failCount)

# Now to check how many "outstanding" students
m = 0
outStudent = 0
while m < Homework.shape[0]:
	if list_Grades[m] > 9.5:
		outStudent = outStudent + 1
	m = m + 1
print ('\nNumber of outstanding students:', outStudent)

#Histogram
num_bins = 10
# the histogram of the data
n, bins, patches = plt.hist(list_Grades, num_bins, facecolor='blue', alpha=0.5)
#get rid of normed=1 from matplotlib.org example, caused problems with y-axis
plt.xlabel('Score')
plt.ylabel('Students')
plt.title(r'Histogram of Student Grades')
# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)


#use this to show plot instead of saving it: plt.show()

#save using a .png, save histogram
plt.savefig('Histogram.png', format = 'png')

