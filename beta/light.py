import cv2
import sys
from phue import Bridge
import urllib.request, json
with urllib.request.urlopen(r"https://www.meethue.com/api/nupnp") as url:
    data = json.loads(url.read().decode())
    internalipaddress = data[0]['internalipaddress']

def change_light( flag,curr, stage ):
    power = 0
    #philips hue light connection
    b = Bridge(internalipaddress)
    #b.connect()
    if ( flag ==0 ):
        power = curr - stage
    else:
        power = curr + stage
    b.set_light(1, 'bri', power)
    return power



