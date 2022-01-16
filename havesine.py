#####################################################################
# This segment uses the input from "ISS_city_lat_lon_data_list.txt" #
#  and the output from the ISS Project2 to calculate the distance   #
#   using the Haversine library to calculate treh distance to       #
#    Richland College.                                              #
#                                                                   #
# References:                                                       #
#   Haversine - https://pypi.org/project/haversine/                 #
#   Floating point number formatting - https://pyformat.info/       #
# Rich Park April 19, 2020                                          #
#####################################################################

import time
from haversine import haversine,Unit


def getLocalTime():
    local_time = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime())
    return local_time

def getSampleData():
    cityList=[]
    rtrnList=[]

    ISS_cities=open("ISS_city_lat_lon_data_list.txt","r")
    for item in ISS_cities:
        item=item.strip()
        cityList.append(item.split(","))
    ISS_cities.close()
    
    for item in range(len(cityList)):
        latitude=cityList[item][2]
        longitude=cityList[item][3]
        rtrnList.append(list((latitude, longitude)))
    return(rtrnList)


def DistToRLC(ISS_Position):
    richlandcollege=(32.9214, -96.7285) #Location to Richland College Do not Change
    lat=float(ISS_Position[0])
    long=float(ISS_Position[1])
    ISS_Position=(lat, long)
    ISS_Dist=(haversine(ISS_Position, richlandcollege,Unit.MILES))
    ISS_Dist = ("{:0.1f}".format(ISS_Dist))
    return ISS_Dist

def simISS_Out():
    timeDelay=(1)
    ISS_Data=(getSampleData())

    for i in range (len(ISS_Data)):
        ISS_Distance=DistToRLC(ISS_Data[i])
        lat=float(ISS_Data[i][0])
        long=float(ISS_Data[i][1])

        if (lat < 0) and (long < 0):
            print("On",getLocalTime(), "the ISS is",ISS_Distance, "miles from Richland College")
            print("ISS Latitude =", ISS_Data[i][0]+"; ISS Longitude =", ISS_Data[i][1]+",")
            print("The ISS is south of the Equater, and west of the Prime Meridian.", ("\n"))

        time.sleep(timeDelay)

        if (lat > 0) and (long > 0):
            print("On",getLocalTime(), "the ISS is",ISS_Distance, "miles from Richland College")
            print("ISS Latitude =", ISS_Data[i][0]+"; ISS Longitude =", ISS_Data[i][1]+",")
            print("The ISS is north of the Equater, and east of the Prime Meridian.", ("\n"))

        time.sleep(timeDelay)

        if (lat < 0) and (long > 0):
            print("On",getLocalTime(), "the ISS is",ISS_Distance, "miles from Richland College")
            print("ISS Latitude =", ISS_Data[i][0]+"; ISS Longitude =", ISS_Data[i][1]+",")
            print("The ISS is south of the Equater, and east of the Prime Meridian.", ("\n"))

        time.sleep(timeDelay)

        if (lat > 0) and (long < 0):
            print("On",getLocalTime(), "the ISS is",ISS_Distance, "miles from Richland College")
            print("ISS Latitude =", ISS_Data[i][0]+"; ISS Longitude =", ISS_Data[i][1]+",")
            print("The ISS is north of the Equater, and west of the Prime Meridian.", ("\n"))

        time.sleep(timeDelay)
simISS_Out()