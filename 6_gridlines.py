import matplotlib.pyplot as plt 
import numpy as np

'''
#adding grid lines to plot via "grid()"
x  = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240, 250, 260, 270, 290, 300, 310, 320, 330, 340])  
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.plot(x,y)
plt.title("Health monitor",fontdict=font1)
plt.xlabel("Average oxygen",fontdict=font2)
plt.ylabel("our calorie",fontdict=font2)
plt.grid()
plt.show()



#which grid lines to display via x-axis or y-axis

x  = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240, 250, 260, 270, 290, 300, 310, 320, 330, 340])  
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.plot(x,y)
plt.title("Health monitor",fontdict=font1)
plt.xlabel("Average oxygen",fontdict=font2)
plt.ylabel("our calorie",fontdict=font2)
plt.grid(axis='x')
plt.show()

'''

#setting up line property for grid

x  = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240, 250, 260, 270, 290, 300, 310, 320, 330, 340])  
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.plot(x,y)
plt.title("Health monitor",fontdict=font1)
plt.xlabel("Average oxygen",fontdict=font2)
plt.ylabel("our calorie",fontdict=font2)
plt.grid(color = 'green',ls = '--',lw=0.5)
plt.show()
