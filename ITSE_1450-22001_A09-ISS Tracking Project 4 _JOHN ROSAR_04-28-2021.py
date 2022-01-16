#####################################################################
# John Rosar                                                        #
# ITSE 1450                                                         #
# Project 4                                                         #
# 4-28-21                                                           #    
#####################################################################

import requests
import time
from haversine import haversine,Unit

# City locations (lat, long in Decimal Degrees)
richlandcollege=(32.9214, -96.7285)
print("")
choice = input("Enter '1' for Simulated ISS Position data or '2' for Realtime ISS Position data. ")
if choice == "1":
    print("")
    print("")
    print("################################################################################################")
    print("#   TEST AND VERIFICATION DATA CALCULATED BETWEEN FOUR GLOBAL POSITIONS TO RICHLAND COLLEGE    #")
    print("#                     Rio de Janeiro-BR, Hong Kong-HK, Sydney-AU, Waco-US                      #")
    print("#                      PRESS CONTROL-C (CTRL-C) TO INTERRUPT THE OUTPUT                        #")
    print("################################################################################################")
    print("")


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
        richlandcollege=(32.9214, -96.7285)
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
                print("The ISS is South of the Equater, and West of the Prime Meridian.", ("\n"))

            time.sleep(timeDelay)

            if (lat > 0) and (long > 0):
                print("On",getLocalTime(), "the ISS is",ISS_Distance, "miles from Richland College")
                print("ISS Latitude =", ISS_Data[i][0]+"; ISS Longitude =", ISS_Data[i][1]+",")
                print("The ISS is North of the Equater, and East of the Prime Meridian.", ("\n"))

            time.sleep(timeDelay)

            if (lat < 0) and (long > 0):
                print("On",getLocalTime(), "the ISS is",ISS_Distance, "miles from Richland College")
                print("ISS Latitude =", ISS_Data[i][0]+"; ISS Longitude =", ISS_Data[i][1]+",")
                print("The ISS is South of the Equater, and East of the Prime Meridian.", ("\n"))

            time.sleep(timeDelay)

            if (lat > 0) and (long < 0):
                print("On",getLocalTime(), "the ISS is",ISS_Distance, "miles from Richland College")
                print("ISS Latitude =", ISS_Data[i][0]+"; ISS Longitude =", ISS_Data[i][1]+",")
                print("The ISS is North of the Equater, and West of the Prime Meridian.", ("\n"))

            time.sleep(timeDelay)
    simISS_Out()

if choice == "2":
    print("")
    print("")
    print("#################################################################################################")
    print("#             HAVERSINE CALCULATED ISS DISTANCE FROM THE ISS TO RICHLAND COLLEGE                #")
    print("#                 Four queries at 10 Second intervals will display the data                     #")
    print("#                     PRESS CONTROL-C (CTRL-C) TO INTERRUPT THE OUTPUT                          #")
    print("#################################################################################################")
    print("")
    def getLocalTime(): # Function to get the local time for time stamps
        local_time = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime())
        return local_time
    def getISS_Position(): # Query Open APIs From Space for ISS position
        url = 'http://api.open-notify.org/iss-now'
        json_data = requests.get(url).json()

    # Show raw JSON object. Uncomment this line to view JSON data for testing
    # print(json_data,'\n') 

    # Extract the current ISS lat/long information using Python list/dictionary
    # and convert the string to float data
        iss_lat = float((json_data['iss_position'])['latitude'])
        iss_long = float((json_data['iss_position'])['longitude'])
        iss_latlong = (iss_lat, iss_long)
        return iss_latlong

    def getISS_Distance(ISS_Posit):
        distance = haversine (ISS_Posit, richlandcollege,Unit.MILES)
        return distance

    ISS_Dist=getISS_Distance(getISS_Position())


    def getLocation(ISS_Posit):
        print("ISS Latitude =", ISS_Posit[0], "; ISS Longitude =", ISS_Posit[1])
        if (ISS_Posit[0]) < 0 and (ISS_Posit[1] < 0):
            print("The ISS is South of the Equator and West of the Prime Meridian")
        if (ISS_Posit[0]) < 0 and (ISS_Posit[1] > 0):
            print("The ISS is South of the Equator and East of the Prime Meridian")
        if (ISS_Posit[0]) > 0 and (ISS_Posit[1] < 0):
            print("The ISS is North of the Equator and West of the Prime Meridian")
        if (ISS_Posit[0]) > 0 and (ISS_Posit[1] > 0):
            print("The ISS is North of the Equator and East of the Prime Meridian")
    for interval in range(4):
        print("On", getLocalTime(), "the ISS is","{:0.1f}".format(ISS_Dist),"miles from Richland College")
        getLocation(getISS_Position())
        print("")
        time.sleep(10)
