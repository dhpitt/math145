# David Pitt
# Math 145, HW1 
# draws 1-cycles as described in p2

import matplotlib.pylab as plt
import math
import numpy as np


def E(n,k):
    # generates a 1-cycle
    vertices = []
    for i in range(1,n+k):
        vertices.append([np.cos(2*math.pi*i/n), np.sin(2*math.pi*i/n)])
    return vertices
    

v = E(10,5)
ax = plt.subplot()

ax.plot([x[0] for x in v],[x[1] for x in v],'ro',ms=5)

plt.show()


np.list()

    