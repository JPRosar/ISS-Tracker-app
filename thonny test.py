###########################################################
# John Rosar                                              #
# ITSE 1450-22001                                         #
# Project 5                                               #
# 5-8-21                                                  #
###########################################################

import requests
from haversine import haversine,Unit
import time
from turtle import *


def ISSturtlePlotSetup(): # Graphical display program
    mode('logo') # Logo coordinates N=0°; S=180°; E=90°; W=270°; 
    style = ('Times', 40, 'bold') # Set type style
    style1 = ('Times', 20, 'italic')


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
    write("John Rosar's Graphical ISS Tracker", font=style, align='center')
    setposition(0,315)
    write("Light Blue =  8500 + Miles; Green = 6000 - 8499 Miles", font=style1, align='center')
    setposition(0,275)
    write("Yellow = 1000 - 5999 Miles; Red 0 - 999 Miles", font=style1, align='center')
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

# End Test run

def getISS_Position(): # Query Open Notify APIs From Space for ISS position
    url = 'http://api.open-notify.org/iss-now'
    json_data = requests.get(url).json()
    #print(json_data,'\n') # Show raw JSON object. This line for viewing raw JSON data for testing
 
    # Extract the current ISS lat/long information using Python list/dictionary
    # and convert the string to float data
    iss_lat = float((json_data['iss_position'])['latitude'])
    iss_long = float((json_data['iss_position'])['longitude'])
    iss_latlong = (iss_lat, iss_long) # Return as a tuple
    return iss_latlong

richlandcollege=(32.9214, -96.7285)
waco=(31.5597,-97.1882)
issPosition=getISS_Position()


issDistance=(haversine(issPosition, richlandcollege,Unit.MILES)) # haversine calulation
issDistance=("{:0.1f}".format(issDistance)) #format for 1 decimal place



ISSturtlePlotSetup() # Setup Graphical Tracking window

# Test distance values for substituting the input from
#  simulated or actual ISS distances for verification.
ISS1=9000  #Example Test Data
ISS2=7345  #Example Test Data
ISS3=3756  #Example Test Data
ISS4=473   #Example Test Data
ISS5= (int(haversine(issPosition, richlandcollege,Unit.MILES))) #Real ISS Data
def getISS_Distance(ISS_Posit):
    distance = haversine (ISS_Posit, richlandcollege,Unit.MILES)
    return distance

ISS_Dist=getISS_Distance(getISS_Position())


def getLocation(ISS_Posit):
    for i in range(6):
        print("")
        print("The current ISS distance to Richland College is","{:0.1f}".format(ISS_Dist))
        print("The current Lat/Long of the ISS ->", ISS_Posit)
        print("")
        if (ISS_Posit[0]) < 0 and (ISS_Posit[1] < 0):
            ISSturtlePlotSW(ISSdistColor(ISS5))
            time.sleep(3)
        if (ISS_Posit[0]) < 0 and (ISS_Posit[1] > 0):
            ISSturtlePlotSE(ISSdistColor(ISS5))
            time.sleep(3)
        if (ISS_Posit[0]) > 0 and (ISS_Posit[1] < 0):
            ISSturtlePlotNW(ISSdistColor(ISS5))
            time.sleep(3)
        if (ISS_Posit[0]) > 0 and (ISS_Posit[1] > 0):
            ISSturtlePlotNE(ISSdistColor(ISS5))
            time.sleep(3)
        

getLocation(getISS_Position())


