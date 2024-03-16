#pie chart

import matplotlib.pyplot as plt
import numpy as np

'''
y = np.array([35,25,25,15])
plt.pie(y)
plt.show()


#labelling
y = np.array([35,25,25,15])
mylabels = ["Apple","Banana","Cherry","Mango"]
plt.pie(y,labels=mylabels)
plt.show()

#startangle parameter - default start angle is at hte x-axis but you can change it 
y = np.array([35,25,25,15])
mylabels = ["Apple","Banana","Cherry","Mango"]
plt.pie(y,labels=mylabels, startangle=90)
plt.show()



#explode the piechart by value
y = np.array([35,25,25,15])
mylabels = ["Apple","Banana","Cherry","Mango"]
myexplode  = [0.2,0,0,0]
plt.pie(y,labels=mylabels, explode=myexplode)
plt.show()


#shadow parameter 
y = np.array([35,25,25,15])
mylabels = ["Apple","Banana","Cherry","Mango"]
myexplode  = [0.2,0,0,0]
plt.pie(y,labels=mylabels, explode=myexplode, shadow=True)
plt.show()


#coloring

y = np.array([35,25,25,15])
mylabels = ["Apple","Banana","Cherry","Mango"]
mycolors = ["black","hotpink","b","#43AF50"]

plt.pie(y,labels=mylabels,  shadow=True,colors=mycolors)
plt.show()

'''
#legends
y = np.array([35,25,25,15])
mylabels = ["Apple","Banana","Cherry","Mango"]

plt.pie(y,labels=mylabels,  shadow=True)
plt.legend(title = "Fruits")
plt.show()





