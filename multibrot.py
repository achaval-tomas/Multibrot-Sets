from pygame import init, display, Vector2, draw, event, quit, QUIT

init() # pygame init

# Time complexity = O(n*p) 
# where n is the total number of points used (in this case width*height)
# and p is the amount of iterations we calculate for each of them.

# Complex numbers c = a + b*i are represented as vectors (a, b)

# General form for a multibrot set
# z_0 = (0, 0)
# given z_0 and a point p, we check the divergence of 
# the set z_(n+1) = (z_n)^exp + p   , n >= 0
# and add the point to the set if it does not diverge to infinity.

# Choose the number of iterations (accuracy as well as processing time increases with it)
# The set becomes perfect as precision tends to infinity. 
# It looks good enough with precision set to 200.
precision = 200

# Choose the Multibrot set exponent
exp = 2

# Choose diplaying step size
# Higher(Lower) step => Faster(Slower) loading animation time
step = 40


# Initialize main constants
width = 1280
height = 720
origin = Vector2(width/2, height/2) # Centered origin

# Set the window up
screen = display.set_mode((width, height))
display.set_caption("Multibrot Set (exp = " + str(exp) + "," 
                               + " precision = " + str(precision) + "," 
                               + " step = " + str(step) + ")")

# Function to draw X and Y axis with respect to origin.
def drawAxis(screen):
    draw.line(screen, "white", (origin.x, 0), (origin.x, height), 1)
    draw.line(screen, "white", (0, origin.y), (width, origin.y), 1)

# Draw the main plane
screen.fill("purple")
drawAxis(screen)
display.flip()

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

# Init empty multibrot set
multibrotset = []

# In this step we pre-compute all the points in the screen which fall within the set bound.
for b in range(-int(origin.y), int(origin.y)):
    for a in range(-int(origin.x), int(origin.x)):

        c = Vector2(a, b) # c = a + b*i

        # Add points that stay bounded
        if setIsBounded(c):
            multibrotset.append(origin + c)  # Point is added as pixel coordinate with respect to the origin.


# draw each point contained in the mandelbrot set.
for i in range(multibrotset.__len__()):

    draw.circle(screen, "black", multibrotset[i], 1)

     # only display the render every 40 points (faster performance).
    if not i%step:
        display.flip()


# Init infloop bool
running = True

# keep window open
while running:

    for e in event.get():
        if e.type == QUIT:
            running = False

quit()