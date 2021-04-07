# David Pitt
# Feb 11, 2020
# Visualization of the straight-line homotopy
# Uses earlier code I wrote as a springboard

from drawComplex import drawLoop,polynomial
import math
import matplotlib.pylab as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as anim
import numpy as np

animRes = 200

##############################
# The straight-line homotopy #
##############################

# This function takes in two loops (lists of complex numbers)
# and outputs a long matrix that shows the continuous deformation
# of one loop into the other. 

p = polynomial(lambda z: z**4 + z**2 - z + 2, r'$p(z) = z^4 + z^2 - z + 2$')

pZ = drawLoop(p,2,1,animRes) 

# lSpace = straightLineHomotopy(circle,Rd)

#print(lSpace)

#######################
# Visualizing results #
#######################
fig,ax = plt.subplots()
plt.plot([x.real for x in pZ],[x.imag for x in pZ],color='blue')
d1, = plt.plot([pZ[0].real,0],[pZ[0].imag,0],marker='o',color='red')

# Animate 
def animateH(i):
    d1.set_data([pZ[i].real,0],[pZ[i].imag,0])

anim = anim.FuncAnimation(fig, animateH, frames=list(range(0,animRes)), \
                                      interval=100, blit=False, repeat=True)

ax.set(xlabel='Re(z)',ylabel='Im(z)')
ax.set(title='w(p(z),0)')
plt.draw()
anim.save('wind1.mp4', fps=60, extra_args=['-vcodec', 'libx264'])