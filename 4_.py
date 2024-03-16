import matplotlib.pyplot as plt 
import numpy as np

'''

#linestyle os ls - is used to change the style of plotted line

ypoints  = np.array([3,8,1,10])

plt.plot(ypoints, ls = 'dotted') #ls  =':'
plt.show()



#linecolor  - c

ypoints  = np.array([3,8,1,10])

plt.plot(ypoints, c= 'r') #ls  =':'
plt.show()


#width of a line  -lw

ypoints  = np.array([3,8,1,10])

plt.plot(ypoints, lw = '20.5') 
plt.show()
'''

#exampe for multiple line
xpoints  = np.array([3,8,1,10])

ypoints  = np.array([6,2,7,11])

plt.plot(xpoints,ls = 'dashed', lw = '15.5', c= 'k') 
plt.plot(ypoints,ls = 'dotted', lw = '19.5', c= 'g') 

plt.show()
