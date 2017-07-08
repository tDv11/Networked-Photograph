import urllib.request, json
import sys
import phue
from phue import Bridge
import random
import time

def uponUs():
    print('DoomsDay is Upon Us')
    
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

    while True:

        my_random_light = random.randint(1, 13)
        my_random_power = random.randint(170, 254)
        b.set_light(my_random_light, 'bri',my_random_power )
        print('light: ' +str(my_random_light)  + ' power: ' +str(my_random_power))
        time.sleep(random.randint(10, 15))

        my_random_power = random.randint(10, 80)
        b.set_light(my_random_light, 'bri',my_random_power )
        print(' next power: ' +str(my_random_power))
        time.sleep(random.randint(5, 10))
