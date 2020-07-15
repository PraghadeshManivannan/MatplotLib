import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,7,4]

a = [1,2,3]
b = [10,14,16]

plt.plot(x,y,label = 'normal')
plt.plot(a,b,label = 'twice multiplied')

plt.xlabel('Plot Number') #labels the x-axis
plt.ylabel('Plot size') #labels the y-axis

plt.title('Graph for reference') #title for the graph

plt.legend() #tells about the which line belong to which condition

plt.show()
