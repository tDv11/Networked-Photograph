import json
import sys
import urllib.request
import phue

import cv2
from phue import Bridge

 # photo attributes
JUMP = 19  
max_power = 254  
min_power = 60
light_id = 1
    
# read bridge ip from web
with urllib.request.urlopen(r"https://www.meethue.com/api/nupnp") as url:
    data = json.loads(url.read().decode())
    ip = data[0]['internalipaddress']
    
# philips hue light connection
while True:
    try:
        b = Bridge(ip)
        break
    except phue.PhueRegistrationException :
        print('please press connect button on bridge')
