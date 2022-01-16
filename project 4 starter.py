#####################################################
# The ISS Query requests information for the next   #
# flyover of the  International Space Station (ISS) #
# ISS API Reference http://open-notify.org/         #
#                                                   #
# Rich Park April 17, 2020                       #
#####################################################


import time
from haversine import haversine,Unit
import requests

CSV_Data="ISS_city_lat_lon_data_list.txt"

def getLocalTime():
    Local_time = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime())
    return Local_time

def GetCities(citydata):
    cityList=[]
    ISS_cities=open(citydata,"r")
    for item in ISS_cities:
        item=item.strip()
        cityList.append(item.split(","))
    ISS_cities.close()
    return cityList

def getISS_Position():
    url = 'http://api.open-notify.org/iss-now.json'
    json_data = requests.get(url).json()
    #print(json_data,'\n')#
    
    iss_Lat = float((json_data['iss_position'])['latitude'])
    iss_Long = float((json_data['iss_position'])['longitude'])
    iss_LatLong = (iss_Lat, iss_Long)
    return iss_LatLong

richlandcollege=(32.9214, -96.7285)
waco=(31.5597,-97.1882)
issPosition=getISS_Position()

issDistance=(haversine(issPosition, richlandcollege,Unit.MILES)) # haversine calulation
issDistance=("{:0.1f}".format(issDistance)) #format for 1 decimal place

print(f"From the ISS to Richland College is {issDistance} miles.") # Distance in Miles


choice = input("Enter '1' for simulated ISS Position data or '2' for realtime ISS Position data. ")
if choice == "1":
    simISS_Position()
if choice == "2":
    repeatISS_Position()