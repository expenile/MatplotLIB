#display the multiple plot -  with subplot() you can draw multiple plot in one figure
import matplotlib.pyplot as plt
import numpy as np
'''

 
#plot1
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,1,1) #the figure has 1 row, 2 columns and this plot is the plot
plt.plot(x,y)


#plot2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,1,2)
plt.plot(x,y)
plt.show()

'''

#now we will draw a challenge of 6 plot
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,3,1) #the figure has 1 row, 2 columns and this plot is the plot
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,3,2)
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,3,3) #the figure has 1 row, 2 columns and this plot is the plot
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,3,4)
plt.plot(x,y)


x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,3,5) #the figure has 1 row, 2 columns and this plot is the plot
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,3,6)
plt.plot(x,y)
plt.show()

