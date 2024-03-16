#histogram is used for frequency distribution

import matplotlib.pyplot as plt
import numpy as np

#example  - say you ask for height of 250 people then how to make a histogram  -hist() function

x = np.random.normal(170,10,250)
plt.hist(x)
plt.show()
