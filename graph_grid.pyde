# This script will plot a grid for a graph

# Source code/software
    # Math Adventures with Python by Peter Farrell, Chapter 4+
    # Made with Processing 3.5.4 using Python Mode in Dec 2021
      # https://py.processing.org/tutorials/
      # https://processing.org/reference/
      # https://github.com/processing

# set the x axis range for the graph
x_min = -10
x_max = 10

# set the y axis range for the graph
y_min = -10
y_max = 10

# calculate the graph axis ranges
x_range = x_max - x_min
y_range = y_max - y_min

def setup():
    """one time function to setup the environment"""
    
    # global variables
    global x_scale, y_scale
    
    # default screen size (display window) in pixels
    size(600,600)
    
    # scaled screen size (display window); width & height are program keywords
    x_scale = width/x_range   # ie 600/(10 - (-10)) = 30
    y_scale = height/y_range
    
def draw():
    """infinite looping function to draw the idea"""
    global x_scale, y_scale
    
    # white background
    background(255)
    
    # move the origin from default top left of screen to center of screen
    translate(width/2, height/2)
    
    # grid line thickness, color (cyan), and quantity (40 = 10 + 10 + 10 + 10)
    strokeWeight(1)
    stroke(0,255,255)
    for i in range(x_min, x_max +1):
        line(i*x_scale, y_min*y_scale, i*x_scale, y_max*y_scale)
        line(x_min*x_scale, i*y_scale, x_max*x_scale, i*y_scale)
