# Code borrowed and modified from these sources
# https://docs.python.org/3.3/library/turtle.html? highlight=turtle#turtle.shape
# Source: https://runestone.academy/runestone/books/published/thinkcspy/PythonTurtle/InstancesAHerdofTurtles.html
# https://stackoverflow.com/questions/19498447/multithreading-with-python-turtle

###########################################################
#  Emerging Technologies Systems Analysis and Design      #
#    Network Programmability with Cisco APIC-EM           #           
#    Final Project - Tracking the ISS with a GUI          #
#      Turtle Graphics Student Dist Fragment              #
#                                                         #
#  Coded by Rich Park 2020-05-02                          #
#                                                         #
###########################################################

import time
from turtle import *


def ISSturtlePlotSetup(): # Graphical display program
    mode('logo') # Logo coordinates N=0°; S=180°; E=90°; W=270°; 
    style = ('Times', 40, 'bold') # Set type style

    # Initialize turtle and set positions
    nw=(-100,100)
    ne=(100,100)
    se=(100,-100)
    sw=(-100,-100)
    reset()
    clear()
    home()

    # Create display grid
    hideturtle()
    penup()
    setposition(0,350)
    write("Prof. Park's Graphical ISS Tracker", font=style, align='center')
    home()
    pendown()
    pensize(5)
    forward(200)
    back(400)
    home()
    left(90)
    forward(200)
    back(400)
    home()
    penup()
    hideturtle()

    # Label the display grid
    setposition(nw)
    write('NW', font=style, align='center')
    setposition(ne)
    write('NE', font=style, align='center')
    setposition(se)
    write('SE', font=style, align='center')
    setposition(sw)
    write('SW', font=style, align='center')
    time.sleep(1)
    hideturtle()

    # Set turtle properties
    shape('triangle')
    turtlesize(3,2,4)
    penup()

# End ISSturtlePlotSetup

def ISSdistColor(ISS_Distance): # Assign turtle fill colors according to distance
    if ISS_Distance >= 8500:
        distColor=('lightblue')
    if ISS_Distance >= 6000 and ISS_Distance <8500:
        distColor=('green')
    if ISS_Distance >= 1000 and ISS_Distance <6000:
        distColor=('yellow')
    if ISS_Distance < 1000:
        distColor=('red')
    return(distColor)
# End ISSdistColor

def ISSturtlePlotNW(distColor):
    # Test the turtle position in the NW quadrant and change fill color
    hideturtle()
    color('black',distColor)
    setposition(-100,75)
    showturtle()
# End ISSturtlePlotNW
    
def ISSturtlePlotNE(distColor):
    # Test the turtle position in the NW quadrant and change fill color
    hideturtle()
    color('black',distColor)
    setposition(100,75)
    showturtle()
# End ISSturtlePlotNE
    
def ISSturtlePlotSE(distColor):
    # Test the turtle position in the NW quadrant and change fill color
    hideturtle()
    color('black',distColor)
    setposition(100,-125)
    showturtle()
# End ISSturtlePlotSE
    
def ISSturtlePlotSW(distColor):
    # Test the turtle position in the SW quadrant and change fill color
    hideturtle()
    color('black',distColor)
    setposition(-100,-125)
    showturtle()
    # End ISSturtlePlotSW
ISSturtlePlotSetup()