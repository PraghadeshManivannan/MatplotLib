import matplotlib.pyplot as plt

x = [1,3,5,7,9]
y = [2,4,6,8,10]

b = [1,3,5,7,9]
a = [2,4,6,8,10]

plt.bar(x,y,label = 'Bar graph 1',color = 'b')
plt.bar(a,b,label = 'Bar graph 2',color = 'c')

plt.xlabel('x')
plt.ylabel('y') 

plt.title('Bar graph') 

plt.legend()

plt.show()
