import telnetlib
import time
import sys
import pymongo
import random
import datetime

URI = 'mongodb://net_photo:net.photo456@ds139322.mlab.com:39322/net_photographs'
last_A = 0
last_B = 0

client = pymongo.MongoClient(URI)
db = client['net_photographs']
simulation = db.sessions

host= (b"10.0.0.100 23")
user = (b'user1')
password = (b'user1')

tn = telnetlib.Telnet('10.0.0.100','23')

#print(tn.read_all())

tn.write(('user1\x0d\x0a').encode('ascii'))

#print(tn.read_all())

tn.write(('user1\x0d\x0a' ).encode('ascii'))

#print(tn.read_all())
while True:
    print('call to DB as started ' + str(datetime.datetime.now()))
    cursor_one = simulation.find({'photoID':1})
    for doc in cursor_one:
        face_one = doc['currentViewers']

    cursor_two = simulation.find({'photoID':2})
    for doc in cursor_two:
        face_two = doc['currentViewers']

    cursor_three = simulation.find({'photoID':3})
    for doc in cursor_three:
        face_three = doc['currentViewers']

    cursor_four = simulation.find({'photoID':4})
    for doc in cursor_four:
        face_four = doc['currentViewers']

    cursor_five = simulation.find({'photoID':5})
    for doc in cursor_five:
        face_five = doc['currentViewers']

    cursor_six = simulation.find({'photoID':6})
    for doc in cursor_six:
        face_six = doc['currentViewers']

    cursor_seven = simulation.find({'photoID':7})
    for doc in cursor_seven:
        face_seven = doc['currentViewers']

    cursor_eight = simulation.find({'photoID':8})
    for doc in cursor_eight:
        face_eight = doc['currentViewers']

    cursor_nine = simulation.find({'photoID':9})
    for doc in cursor_nine:
        face_nine = doc['currentViewers']

    cursor_ten = simulation.find({'photoID':10})
    for doc in cursor_ten:
        face_ten = doc['currentViewers']

    cursor_eleven = simulation.find({'photoID':11})
    for doc in cursor_eleven:
        face_eleven = doc['currentViewers']

    cursor_twelve = simulation.find({'photoID':12})
    for doc in cursor_twelve:
        face_twelve = doc['currentViewers']

    cursor_thirteen = simulation.find({'photoID':13})
    for doc in cursor_thirteen:
        face_thirteen = doc['currentViewers']
    print('call to db as ended ' +str(datetime.datetime.now()))
    A = face_one + face_two + face_three + face_four + face_five
    B = face_six + face_seven + face_eight + face_nine + face_ten + face_eleven + face_twelve + face_thirteen
    if( A + B == 0  ) or ( last_A+last_B == A+B ):
        tn.write(('#output,81,1,65\x0d\x0a').encode('ascii'))
        tn.write(('#output,84,1,35\x0d\x0a').encode('ascii'))
        print('there was no move in the gallery, light is set to 65/35')
        time.sleep(random.randint(20, 35))
        tn.write(('#output,84,1,65\x0d\x0a').encode('ascii'))
        tn.write(('#output,81,1,35\x0d\x0a').encode('ascii'))
        print('north and south lights power have been switch')
        time.sleep(random.randint(20, 30))
    else:
        first_power = int((A*100)/(A+B))
        second_power = int(100 - A)
        tn.write(('#output,81,1,' + str(first_power) + '\x0d\x0a').encode('ascii'))
        tn.write(('#output,84,1,' + str(second_power) + '\x0d\x0a').encode('ascii'))
        print('north light is: ' + str(first_power))
        print('southy light is : ' +str(second_power))

    last_A = A
    last_B = B
    #sess_op = tn.read_all()
    #print (sess_op)

sys.exit()





# 84: south (6-13)
# 81: north (1-5)
# 83: center entrance (not in use)
