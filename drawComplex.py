# David Pitt
# This is part of a toolkit I wrote
# to draw curves in the complex plane
# to help me do my homeworks.

import matplotlib.pylab as plt
import numpy as np
import math


def complexCurve1(poly,res=314):
    # Draws a curve for a given complex polynomial
    # on the C plane.
    tspace = np.linspace(0,1,res+1)
    Zs = []
    pZ = []
    for t in tspace:
        Zs.append(np.exp(2*math.pi*1j*t))

    for z in Zs:
        pZ.append(poly(z))

    X = [x.real for x in pZ]
    Y = [x.imag for x in pZ]
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
complexCurve1(p1)

p2 = polynomial(lambda z: z**4 - 2*z**3 + z**2 - z + 2, r'$p(z) = z^4 - 2z^3 + z^2 - z + 2$')
complexCurve1(p2)



