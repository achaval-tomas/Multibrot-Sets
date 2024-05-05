from pygame import Vector2

# Choose the number of iterations (accuracy as well as processing time increases with it)
# The set becomes perfect as precision tends to infinity. 
# It looks good enough with precision set to 200.
precision = 200

# Choose the Multibrot Set exponent
exp = 2

# Choose diplaying step size
# Higher(Lower) step => Faster(Slower) loading animation time
step = 40


# Initialize main constants
width = 1280
height = 720
origin = Vector2(width/2, height/2) # Centered origin