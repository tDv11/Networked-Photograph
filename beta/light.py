import cv2
import sys
from phue import Bridge
import urllib.request, json

# every person add 42 to power
jump = 42
lightid = 1
#read brigde ip from web
with urllib.request.urlopen(r"https://www.meethue.com/api/nupnp") as url:
    data = json.loads(url.read().decode())
    ip = data[0]['internalipaddress']
    id = data[0]['id']

def change_light( prevfaces, curr, prevpower):
    #philips hue light connection
    b = Bridge(ip)
    #b.connect()
    power = 60
    diff = 0
    
    if( prevfaces > curr ):
        diff = prevfaces - curr
        power += jump * ( prevpower - diff )


    if ( prevfaces < curr ):
        diff = curr - prevfaces
        power += jump * ( curr + diff )
        
    if( power > 254 ):
        power = 254
    b.set_light(lightid, 'bri', power)
    prevpower = power
    prevfaces = curr
