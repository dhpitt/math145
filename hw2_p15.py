# David Pitt
# Feb 9, 2021
# Math 145 HW 2

# Problem 15
from drawComplex import polynomial,drawGammaR_1
import numpy as np
import math

poly = polynomial(lambda z: 9 + 3*z+ 22*z**2 - 17*z**3 + 3*z**4, r'$9 + 3z + 22z^2 - 17z^3+ 3z^4$')

q = polynomial(lambda z: poly(z+3), r'$q(z) = p(z+3)$')
c = polynomial(lambda z: z, r'$z$')

v = polynomial(lambda z: poly(z-19/6-math.sqrt(11)/6*1j), r'$q(z) = p(z-1/6- \frac{\sqrt{11}}{6}}i)$')
#drawGammaR_1(poly,2)
#drawGammaR_1(poly,5)

# i) Show that p has a double root at 3, and then determine all 4 roots of p.

#drawGammaR_1(poly,3)
#drawGammaR_1(q,-19/6+math.sqrt(11)/6*1j)
#drawGammaR_1(q,-19/6-math.sqrt(11)/6*1j)
drawGammaR_1(q)
drawGammaR_1(poly)
drawGammaR_1(c)
drawGammaR_1(v)

