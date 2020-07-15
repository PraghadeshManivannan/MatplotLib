import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,6,8,9,10]
eating = [2,3,2,3,4]
working = [7,8,8,5,6]
playing = [8,7,6,7,4]

'''

x,y denotes the data
y will be the list of datas which is to be stacked
label gives the label to the plot
marker denotes the symbol how the scatter plot is to be denoted
s denotes the square of shape
colors will also be in the type of list similar to the list of y

'''

plt.scatter([],[],color = 'm' , label = 'Sleeping' , marker = 's')
plt.scatter([],[],color = 'r' , label = 'Eating' , marker = 's')
plt.scatter([],[],color = 'b' , label = 'Working' , marker = 's')
plt.scatter([],[],color = 'y' , label = 'Playing' , marker = 's')

plt.stackplot(days,sleeping,eating,working,playing,colors = ['m','r','b','y'])

plt.xlabel('Days')
plt.ylabel('Time spent') 

plt.title('Time spent during the days using stackplot') 

plt.legend()
plt.show()
