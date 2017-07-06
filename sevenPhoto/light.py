
import sys
import phue

import cv2
from phue import Bridge


def change_light( prev_faces, curr, prev_power, ip):
      
    # photo attributes
    JUMP = 45
    max_power = 254  
    min_power = 0
    light_id = 7
    
    
    # philips hue light connection
    while True:
        try:
          b = Bridge(ip)
          break  
        except phue.PhueRegistrationException :
            print('please press connect button on bridge')
    
    power = min_power
    diff = 0
    
    if prev_faces > curr :
        diff = prev_faces - curr
        

    if  prev_faces < curr :
        diff = curr - prev_faces

    
    
    power += ( JUMP *  (curr) )
    
    
    # calibrate if overflow
    if power > max_power :
        power = max_power
    if power < min_power :
        power = min_power

    # change light power
    b.set_light(light_id, 'bri', int(power))
    print(power)
    prev_power = power
    prev_faces = curr
    
    return ( prev_faces, prev_power )
