import json
import sys
import urllib.request

import cv2
from phue import Bridge



def change_light( prev_faces, curr, prev_power):
    # photo attributes
    JUMP = 19  # CR: consts should be UPPER_CASE
    max_power = 254  # CR: separate words with underscore `maxpower` => `max_power`
    min_power = 60
    light_id = 1
    
    # read bridge ip from web
    with urllib.request.urlopen(r"https://www.meethue.com/api/nupnp") as url:
        data = json.loads(url.read().decode())
        ip = data[0]['internalipaddress']
    
    # philips hue light connection
    b = Bridge(ip)
    # b.connect()
    power = 0
    diff = 0
    
    if prev_faces > curr :
        diff = prev_faces - curr
        power = JUMP * (prev_power - diff)

    if  prev_faces < curr :
        diff = curr - prev_faces
        power = JUMP * (curr + diff)
    
    # calibrate if overflow    
    if power > maxpower :
        power = maxpower
    if power < minpower :
        power = minpower
    
    # change light power
    b.set_light(lightid, 'bri', power)

    prev_power = power
    prev_faces = curr
    
    return ( prev_faces, prev_power )
