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
CSV_Data="ISS_city_lat_lon_data_list.txt"

def getLocalTime():
    LocalTime = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime())
    return LocalTime

def GetCities(citydata):
	cityList=[]
	ISS_cities=open(citydata,"r")
	for item in ISS_cities:
		item=item.strip()
		cityList.append(item.split(","))
	ISS_cities.close()
	return cityList

def FormatCities(file):
    for i in range(len(file)):
        richlandcollege=(32.9214, -96.7285)
        LocalTime= getLocalTime()
        Lat=float((file[i][2]))
        Long=float((file[i][3]))
        issPosition=(Lat, Long)
        issDistance=(haversine(issPosition, richlandcollege, Unit.MILES))
        issDistance=("{:0.1f}".format(issDistance))
        if Lat>0:
            LatPos="North"
        else:
            LatPos="South"
        if Long > 0 and Long < 180:
            LongPos="East"
        else:
            LongPos="West"
        
        # Comment/Uncomment
        #print(f"{city}, {country}: Latitude = {lat}; Longitude = {long}.")
        #print(f"{city} is {latPos} of the Equater, and {longPos} of the Prime Meridian.\n")

        print(f"On {LocalTime} the ISS is {issDistance} miles from Richland College. ")
        print(f"ISS Latitude = {Lat}; ISS Longitude = {Long}.")
        print(f"The ISS is {LatPos} of the Equater, and {LongPos} of the Prime Meridian. \n")
        time.sleep(2)
FormatCities(GetCities(CSV_Data))