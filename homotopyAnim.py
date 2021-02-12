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

def straightLineHomotopy(loop1,loop2):
    loopSpace = []

    slices = np.linspace(0,1,animRes)
    
    for s in slices:
        loopSpace.append([s*loop2[i] + (1-s)*loop1[i] for i in range(len(loop1))])
    return loopSpace

# Create data
p1 = polynomial(lambda z: z, r'$p(z) = z$')
p2 = polynomial(lambda z: z**4 + z**2 - z + 2, r'$p(z) = z^4 + z^2 - z + 2$')

pZ = drawLoop(p2,2,1,animRes) # p(2e^(2*pi*i*t))
circle = drawLoop(p1,2,1,animRes) # 2e^(2*pi*i*t)
Rd = drawLoop(p1,2,4,animRes) # 2^d*e^(8*pi*i*t)

lSpace = straightLineHomotopy(pZ,Rd)
# lSpace = straightLineHomotopy(circle,Rd)

#print(lSpace)

#######################
# Visualizing results #
#######################
fig,ax = plt.subplots()
d1, = plt.plot([x.real for x in lSpace[0]],[x.imag for x in lSpace[0]],color='blue')
d2, = plt.plot([x.real for x in lSpace[animRes-1]],[x.imag for x in lSpace[animRes-1]],color='red')

# Animate 
def animateH(i):
    d1.set_data([x.real for x in lSpace[i]],[x.imag for x in lSpace[i]])

anim = anim.FuncAnimation(fig, animateH, frames=list(range(0,animRes)), \
                                      interval=100, blit=False, repeat=True)

ax.set(xlabel='Re(z)',ylabel='Im(z)')
ax.set(title='Map from the circle to d=3')
plt.draw()
anim.save('slh_6.mp4', fps=60, extra_args=['-vcodec', 'libx264'])