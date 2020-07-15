import matplotlib.pyplot as plt

ages = [22,50,21,35,41,36,32,26,46,19,29,54,98,94,74,65,26,35,84,65,56,36,56,58,42]

'''
bins denotes the range of distribution that is the difference between the bars
hist type denotes how the histogram wants to be drawn
rwidth denotes the width of the bar
color denotes color of the bar which is to be shown
'c' denotes 'CYAN'

'''

plt.hist(ages,bins = 10,histtype = 'bar',rwidth = 0.8,color = 'c')

plt.xlabel('Age distribution')
plt.ylabel('Age') 

plt.title('Age distribution histogram') 

plt.show()
