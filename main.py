# import astropy as ap
import astropy_healpix as hp

'''
# option 1: detect automatically, based on the device IP 
# (can have discrepancy from the real location) requesting an online service
# in case of frequent requests throws "HTTPError: 429 Client Error: 
# Too Many Requests for url: https://api.ipregistry.co/"
from ipregistry import IpregistryClient
import json
client = IpregistryClient("tryout")
ipInfo = client.lookup()
j_ipInfo = json.loads(ipInfo)
latitude = j_ipInfo["location"]["latitude"]
longitude = j_ipInfo["location"]["longitude"]
'''

# option 2: manually enter the address of the observer
import geopy as gpy
locator = gpy.Nominatim(user_agent='myGeocoder')
location = locator.geocode('Toronto, Ontario, Canada')
# print('Latitude = {}, Longitude = {}'.format(location.latitude, location.longitude))
Latitude = location.latitude
Longitude = location.longitude

# obj = hp.HEALPix(nside=12)
# obj.cone_search_lonlat('10', '10', 5)
