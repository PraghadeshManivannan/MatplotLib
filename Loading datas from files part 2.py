import matplotlib.pyplot as plt
import numpy as np

'''
loadtxr -> loads the text file
delimiter -> the values which have been used to separate the values
unpack -> unpacking the entire values as list
'''

x,y = np.loadtxt('example.txt', delimiter = ',' ,unpack = True)

plt.plot(x,y,'y',label = 'Loading the file using numpy')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Loading data from text file')

plt.show()
