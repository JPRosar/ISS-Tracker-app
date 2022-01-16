# John Rosar
# ITSE-1450-22001
# 04/15/21
# A07-ISS Tracking Project 2


import time

cityList=[]
ISS_cities=open("ISS_city_lat_lon_data_list.txt","r")
for item in ISS_cities:
   item=item.strip()
   # The .split method uses the comma to create lists within cityList
   cityList.append(item.split(","))
ISS_cities.close()
print("List of Sample ISS Data Points.")

for i in range(len(cityList)):
    while len(cityList[i])>2:
        cityList[i].pop(0)
    print(cityList[i])
print()
print("ISS_Data list length = ", len(cityList) )
print()
CSV_Data="ISS_city_lat_lon_data_list.txt"

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
        city=(file[i][0])
        country=(file[i][1])
        Lat=float((file[i][2]))
        Long=float((file[i][3]))
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

        print(f"ISS Latitude = {Lat}; ISS Longitude = {Long}.")
        print(f"The ISS is {LatPos} of the Equater, and {LongPos} of the Prime Meridian.\n")
        time.sleep(1)
FormatCities(GetCities(CSV_Data))

