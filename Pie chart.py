import matplotlib.pyplot as plt


'''
slices will be the data which have been used for the pie-chart
label gives the label to the plot
colors will also be in the type of list similar to the list of datas
startangle -> denotes the angle which the pie has to be started
shadow -> to give shadow to the pie chart
explode -> helps the division to be exposed somehow different than that are not exploded
autopct -> converts the values into percentage

'''

slices = [10,4,6,4]
activities = ['Sleeping','Eating','Working','Playing']

plt.pie(slices,labels = activities, colors = ['m','r','c','y'], startangle = 0, shadow = True, explode = (0,0,0.1,0) , autopct = '%1.1f%%')

plt.title('Time spent during a day using pie chart') 

plt.show()
