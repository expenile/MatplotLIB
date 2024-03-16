import matplotlib.pyplot as plt 
import numpy as np
'''
#Create labels for plot
x  = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,290,300,310,320,330])
plt.plot(x,y)
plt.xlabel("Average oxygen")
plt.ylabel("our calorie")
plt.show()



#creating title for the plot
x  = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240, 250, 260, 270, 290, 300, 310, 320, 330, 340])  # Added a hypothetical value to match the length of x
plt.plot(x,y)
plt.title("Health monitor")
plt.xlabel("Average oxygen")
plt.ylabel("our calorie")
plt.show()


#Setting the font property for title and label via fontdict
x  = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240, 250, 260, 270, 290, 300, 310, 320, 330, 340])  
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.plot(x,y)
plt.title("Health monitor",fontdict=font1)
plt.xlabel("Average oxygen",fontdict=font2)
plt.ylabel("our calorie",fontdict=font2)
plt.show()

'''
#changing the location of title
x  = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240, 250, 260, 270, 290, 300, 310, 320, 330, 340])  
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.plot(x,y)
plt.title("Health monitor",fontdict=font1,loc='left')
plt.xlabel("Average oxygen",fontdict=font2)
plt.ylabel("our calorie",fontdict=font2)
plt.show()

