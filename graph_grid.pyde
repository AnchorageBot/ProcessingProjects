# This script will plot a grid for a graph

# Source code/inspiration/software
    # Math Adventures with Python by Peter Farrell, Chapter 4+
    # Processing 3.5.4, Python Mode
    # https://github.com/processing

# set the x-value range
x_min = -10
x_max = 10

# set the y-value range
y_min = -10
y_max = 10

# calculate the graph range
x_range = x_max - x_min
y_range = y_max - y_min

def setup():
    global x_scale, y_scale
    size(600,600)
    x_scale = width/x_range
    y_scale = height/y_range
    
def draw():
    global x_scale, y_scale
    # white background
    background(255)
    translate(width/2, height/2)
    # cyan grid lines
    strokeWeight(1)
    stroke(0,255,255)
    for i in range(x_min, x_max +1):
        line(i*x_scale, y_min*y_scale, i*x_scale, y_max*y_scale)
        line(x_min*x_scale, i*y_scale, x_max*x_scale, i*y_scale)
