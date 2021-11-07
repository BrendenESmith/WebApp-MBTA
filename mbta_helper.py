import urllib.request
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "Ex93flIArrOmlQSA0ncpLwMPd9SlcVoO"
MBTA_API_KEY = "51c6372aa69047a8b8c16271e877e968"

# url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'
# f = urllib.request.urlopen(url)
# response_text = f.read().decode('utf-8')
# response_data = json.loads(response_text)
# pprint(response_data)


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data

# pprint(get_json(f"http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College"))

place_name = "fenway park"
if " " in place_name:
    place_name = place_name.replace(" ", "%20")
    print(place_name)
location_data = (get_json(f"http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name}"))
#pprint(location_data)
locations = location_data["results"][0]["locations"]
pprint((locations))
print()
print()
for i in range(len(locations)):
    if (locations[i]["adminArea3"]) == 'MA':
        lat_long1 = locations[i]["latLng"]
        print(lat_long1)
# lat_long = tuple(lat_long1.values())
# print(lat_long)
# print(type(lat_long))

# def get_lat_long(place_name):
#     """
#     Given a place name or address, return a (latitude, longitude) tuple
#     with the coordinates of the given place.
#     See https://developer.mapquest.com/documentation/geocoding-api/address/get/
#     for Mapquest Geocoding  API URL formatting requirements.
#     """
#     if " " in place_name:
#         place_name = place_name.replace(" ", "%20")
#     location_data = (get_json(f"http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name}"))
#     #pprint(location_data)
#     locations = location_data["results"][0]["locations"]
#     for i in range(len(locations)):
#         if (locations[i]["adminArea3"]) == 'MA':
#             lat_long = locations[i]["displayLatLng"]
#             break
#     lat_long = tuple(lat_long.values())
#     return lat_long

# print(get_lat_long("fenway park"))
# def get_nearest_station(latitude, longitude):
#     """
#     Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
#     tuple for the nearest MBTA station to the given coordinates.
#     See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
#     formatting requirements for the 'GET /stops' API.
#     """
#     pass

# # Main function (the only funcion that needs to be imported to flask); combination of functions above
# def find_stop_near(place_name):
#     """
#     Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
#     """
#     pass


# def main():
#     """
#     You can test all the functions here
#     """
#     pass


# if __name__ == '__main__':
#     main()
