from pygame import init, display, Vector2, draw, event, time, quit, QUIT
from maths import *
from setup import *

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

# In this step we pre-compute all the points in the screen which fall within the set bound.
for b in range(-int(origin.y), int(origin.y)):
    for a in range(-int(origin.x), int(origin.x)):

        c = Vector2(a, b) # c = a + b*i

        # Add points that stay bounded
        if setIsBounded(c):
            draw.circle(screen, "black", origin + c, 1)
            if not a%step:
                display.flip()

# Init infloop bool
running = True

# keep window open
while running:
    time.wait(500)
    for e in event.get():
        if e.type == QUIT:
            running = False

quit()