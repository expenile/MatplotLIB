import matplotlib.pyplot as plt 
import numpy as np

'''
#you can use argument marker to emphasize each point with specified marker
ypoints  = np.array([3,8,1,10])
plt.plot(ypoints, marker = '*')
plt.show()



#format strings "fmt"  - marker|line|color
ypoints  = np.array([3,8,1,10])
plt.plot(ypoints, 'o:r')
plt.show()

# line reference

#  - solid line
#  : dotted line
#  -- dashed line
#   -. dashline/dotted line


#color reference

#r-red
#g-green
#b-blue
#c-cyan
#m-migenta
#y-yellow
#k-black
#w-white




# marker size  - ms

ypoints  = np.array([3,8,1,10])
plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()



#marker color  -mec(marker edge color)
ypoints  = np.array([3,8,1,10])
plt.plot(ypoints, marker = 'o', ms = 20,mec = 'r')
plt.show()


'''
#marker face color -mfc(we can give any color like hex, colorname)
ypoints  = np.array([3,8,1,10])
plt.plot(ypoints, marker = 'o', ms = 20,mfc = 'r',mec ='k')
plt.show()





