#scatter  - the scatter() function one dot for each observation
import matplotlib.pyplot as plt
import numpy as np

'''
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x,y)
plt.show()



#now we will compare 2 plots on same figure -day1

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x,y)



#day2, the age and speed 

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,186,287,188,111,86,103,87,94,78,177,81,80])
plt.scatter(x,y,color = 'pink')
plt.show()





#now we will create a color array , and specify a colormap in scatter plot
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,186,287,188,111,86,103,87,94,78,177,81,80])
colors = np.array([0,10,20,30,40,50,60,70,80,90,100,45,55])

plt.scatter(x,y, c=colors, cmap='viridis')
plt.show()



#you can also include color bar
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,186,287,188,111,86,103,87,94,78,177,81,80])
colors = np.array([0,10,20,30,40,50,60,70,80,90,100,45,55])

plt.scatter(x,y, c=colors, cmap='viridis')
plt.colorbar()
plt.show()



#changing the size 

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,186,287,188,111,86,103,87,94,78,177,81,80])
sizes = np.array([20,50,100,200,500,1000,450,234,123,321,456,167,777])

plt.scatter(x,y, s= sizes)
plt.show()


#alpha - transparency

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,186,287,188,111,86,103,87,94,78,177,81,80])
sizes = np.array([20,50,100,200,500,1000,450,234,123,321,456,167,777])

plt.scatter(x,y, s= sizes,alpha=0.5)
plt.show()

'''


#combine color ,size and alpha
x = np.random.randint(100,size=(100))
y = np.random.randint(100,size=(100))
colors = np.random.randint(100,size=(100))
size = 10* np.random.randint(100,size=(100))
plt.scatter(x,y,c = colors,s = size,alpha=0.5, cmap='nipy_spectral') 
plt.colorbar()
plt.show()

