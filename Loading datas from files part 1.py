import matplotlib.pyplot as plt
import csv

x = []
y = []

'''
opening the text file and accessing the entire values in the list
'''

with open('example.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')

    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))


plt.plot(x,y, 'y' , label = 'Loaded from the text file')


plt.xlabel('x')
plt.ylabel('y')
plt.title('Loading data from text file')

plt.show()
