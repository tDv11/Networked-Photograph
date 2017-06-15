import json
import sys
import urllib.request

import cv2
from phue import Bridge

# photo attributes
jump = 19  # CR: consts should be UPPER_CASE
maxpower = 254  # CR: separate words with underscore `maxpower` => `max_power`
minpower = 60
lightid = 1
# CR: wrap with a function
# read bridge ip from web
with urllib.request.urlopen(r"https://www.meethue.com/api/nupnp") as url:
    data = json.loads(url.read().decode())
    ip = data[0]['internalipaddress']
    id = data[0]['id']  # CR: overrides builtin `id` function + unused variable

def change_light( prev_faces, curr, prev_power):
    # philips hue light connection
    b = Bridge(ip)
    # b.connect()
    power = 0
    diff = 0
    
    if( prev_faces > curr ):  # CR: not need for parentheses to surround `if` statements
        diff = prev_faces - curr
        power = jump * (prev_power - diff)

    if ( prev_faces < curr ):
        diff = curr - prev_faces
        power = jump * (curr + diff)
        
    if( power > maxpower ):
        power = maxpower
    if( power < minpower ):
        power = minpower
    b.set_light(lightid, 'bri', power)
    
    # CR: remove excess empty lines
    
    
    
    
    prev_power = power  # CR: this doesn't effect the value outside of the function
    prev_faces = curr
