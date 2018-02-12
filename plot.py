import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

import matplotlib.mlab as mlab  #using matplot
import math                     #using matplot
from scipy.stats import norm                    #using scipy

a=[1.0, 2.0, 5.0, 7.0, 9.0]
b=[7.8, 21.7, 50, 21, 66.7]

########using matplot##############
mu = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x,mlab.normpdf(x, mu, sigma))
###################################


#########using scipy######################

# Plot between -10 and 10 with .001 steps.
#x_axis = np.arange(-10, 10, 0.001)
# Mean = 0, SD = 2.
#plt.plot(x_axis, norm.pdf(x_axis,0,2))

##########################################
plt.title('normal distribution of patch scores', fontsize=20)
plt.xlabel('score')
plt.ylabel('count of patches')

plt.savefig('plot.png', dpi=None, facecolor='w', edgecolor='w',orientation='portrait', papertype=None, format=None,transparent=False, bbox_inches=None, pad_inches=0.1,frameon=None)

