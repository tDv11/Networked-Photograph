import sys
import pymongo


SEED_DATA = [
    {
        'id': 1,
        'name': 'try',
        'measure': 5,
    }
    ]
uri = 'mongodb://net_photo:net.photo456@ds111771.mlab.com:11771/net_photographs'

def main():

    client = pymongo.MongoClient(uri)

    db = client['emotions']

    emotions = db.emotions

    #emotions.insert_many(SEED_DATA)

    #query = {'id': 1}

    
    #emotions.update({'id' : 1}, {'$set': {'name': 'success'}})

    cursor = emotions.find({'id': 1})
    for doc in cursor:
        print('%s' % doc['name'])
    
    #for doc in cursor:
        #print ('there was %s in id: %s and measure is %s ' %
               #(doc['name'], doc['id'], doc['measure']))

    #db.drop_collection('emotions')
    client.close()


main()


Traceback (most recent call last):
  File "/home/pi/FaceTrack-Master/beta/mongodb.py", line 41, in <module>
    main()
  File "/home/pi/FaceTrack-Master/beta/mongodb.py", line 30, in main
    for doc in cursor:
  File "/usr/local/lib/python3.4/dist-packages/pymongo/cursor.py", line 1114, in next
    if len(self.__data) or self._refresh():
  File "/usr/local/lib/python3.4/dist-packages/pymongo/cursor.py", line 1036, in _refresh
    self.__collation))
  File "/usr/local/lib/python3.4/dist-packages/pymongo/cursor.py", line 928, in __send_message
    helpers._check_command_response(doc['data'][0])
  File "/usr/local/lib/python3.4/dist-packages/pymongo/helpers.py", line 210, in _check_command_response
    raise OperationFailure(msg % errmsg, code, response)
pymongo.errors.OperationFailure: not authorized on emotions to execute command { find: "emotions", filter: { id: 1 } }
