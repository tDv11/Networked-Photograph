import urllib.request, json
import sys
import phue
from phue import Bridge
import random
import time
import noDB
import pymongo

try:
    # connect to MongoDB
    URI = 'mongodb://net_photo:net.photo456@ds139322.mlab.com:39322/net_photographs'
    client = pymongo.MongoClient(URI)
    db = client['net_photographs']
    config = db.config

    # read bridge ip from web
    with urllib.request.urlopen(r"https://www.meethue.com/api/nupnp") as url:
        data = json.loads(url.read().decode())
        ip = data[0]['internalipaddress']

    # update bridge ip
    config.update({'id': 1}, {'$set': {'bridgeIP': ip}})
    print('Bridge ip as been updated to the DB')
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
    
except Exception as e:
    print(e)
    noDB.uponUs()
