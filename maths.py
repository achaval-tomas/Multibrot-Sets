from pygame import Vector2
from setup import *

# Complex numbers (as vectors) multiplication.
def cmpxMult(v1, v2):
    return Vector2(v1.x*v2.x - v1.y*v2.y, v1.x*v2.y + v1.y*v2.x)

# Raise vector v to the power of exp with complex multiplication.
def raiseTo(v, exp):
    res = v
    for i in range(1, exp):
        res = cmpxMult(res, v)
    return res

def bounded(v):
    return ((v.x*v.x + v.y*v.y) <= 4)

# Function to determine if a point is part of the mandelbrot set.
def setIsBounded(point):

    z = Vector2();   # Z_0 = (0,0)
    c = point/300.0  # Map int point to float range [-2, 2]

    # Calculate 16 iterations of Z_n+1 = Z_n^2 + c
    for i in range(precision):
        z = raiseTo(z, exp) + c
        if z.x >= 2 or z.y >= 2: # Low-cost break check
            break

    # If absolute value of Z_n is bounded for all n>=0, then c is in the set.
    return bounded(z) 