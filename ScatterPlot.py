import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [2,6,8,7,6,4,6,3]

'''

x,y denotes the data
label gives the label to the plot
marker denotes the symbol how the scatter plot is to be denoted
s denotes the size of the marker

'''
plt.scatter(x,y,label = 'Scatterplot', color = 'c',marker = 'X', s = 200)

plt.xlabel('Number')
plt.ylabel('Number_counts') 

plt.title('Number count distribution scatter plot') 

plt.legend()
plt.show()
