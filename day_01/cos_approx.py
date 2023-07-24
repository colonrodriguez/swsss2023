#!/usr/bin/env python

"""Space 477: Python: I

cosine approximation function
"""
__author__ = 'Stephanie Colón-Rodríguez'
__email__ = 'stephcr@umich.edu'

from math import factorial
from math import pi
import matplotlib.pyplot as plt
import numpy as np


def cos_approx(x, accuracy=10):
    """
    the test function is then summed for n in range(10)
    """
    test = [((-1)**(n)/factorial(2*n))*(x**(2*n)) for n in range(accuracy)]
    return sum(test)

# Will only run if this is run from command line as opposed to imported
if __name__ == '__main__':  # main code block
    print("cos(0) = ", cos_approx(0))
    print("cos(pi) = ", cos_approx(pi))
    print("cos(2*pi) = ", cos_approx(2*pi))
    print("more accurate cos(2*pi) = ", cos_approx(2*pi, accuracy=50))
assert cos_approx(0) < 1+1.e-2 and cos_approx(0) > 1-1.e-2, "cos(0) is not 1"

# PLOT THE EXPONENTIAL FUNCION FROM 0 TO 1
x = np.linspace(0,1)
y = np.exp(x)
plt.plot(x, y)
plt.xlabel('$0 \leq x < 1$')
plt.ylabel('$e^x$')
plt.title('Exponential Function')
plt.show()
