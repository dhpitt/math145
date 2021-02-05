# David Pitt
# This is part of a toolkit I wrote
# to draw curves in the complex plane
# to help me do my homeworks.

import matplotlib.pylab as plt
from matplotlib.pyplot import draw
import numpy as np
import math

# ax = plt.subplot() # Turn on if you want 1 plot

def drawGammaR_1(poly,r=1,res=314):
    # Draws a curve gamma_r for a given complex polynomial
    # on the C plane.
    # The function maps points on the unit circle
    # to the complex plane using p: C --> C

    # generate slices of the interval [0,1]
    tspace = np.linspace(0,1,res+1)

    Zs = []
    pZ = []
    
    # map t to the function r = 1

    for t in tspace:
        Zs.append(r*np.exp(2*math.pi*1j*t))

    for z in Zs:
        pZ.append(poly(z))

    X = [x.real for x in pZ]
    Y = [x.imag for x in pZ]

    # plot the figure
    
    ax = plt.subplot()
    ax.plot(X,Y)
    ax.set_xlabel('$Re(z)$')
    ax.set_ylabel('$Im(z)$')
    plt.axhline(color='black')
    plt.axvline(color='black')
    ax.minorticks_on()
    ax.grid(which='minor', alpha=0.5)
    ax.grid(which='major', alpha=0.5)
    ax.set_title(poly.latex_label)
    plt.show()
    #return X,Y

class polynomial:
    # An object representing a complex polynomial.
    # You can call this like a function but it also
    # contains a LaTeX label for pretty plots.

    def __init__(self, func, latex_label):
        self.func = func
        self.latex_label = latex_label

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

p1 = polynomial(lambda z: z**2 - z, r'$p(z) = z^2  - z$')
# complexCurve1(p1)

p2 = polynomial(lambda z: z**4 + z**2 - z + 2, r'$p(z) = z^4 + z^2 - z + 2$')
drawGammaR_1(p2)
drawGammaR_1(p2,2)



