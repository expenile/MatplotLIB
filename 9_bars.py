#bar plot using bar()
import matplotlib.pyplot as plt
import numpy as np

'''
#vertical bar
x = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])
plt.bar(x,y)
plt.show()


#horizontal bar
x = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])
plt.barh(x,y)
plt.show()


#color of bar
x = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])
plt.barh(x,y,color = 'red')
plt.show()

#changing the bar width(for vertical bar we can give width but not for horizintal)
x = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])
plt.bar(x,y,width=0.5)
plt.show()
'''

x = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])
plt.barh(x,y,height=0.5)
plt.show()






