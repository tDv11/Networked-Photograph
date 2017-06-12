import cv2
import sys
from phue import Bridge

def change_light( flag,curr, stage ):
    power = 0
    #philips hue light connection
    b = Bridge("10.0.9.252")
    #b.connect()
    if ( flag ==0 ):
        power = curr - stage
    else:
        power = curr + stage
    b.set_light(1, 'bri', power)
    return power



