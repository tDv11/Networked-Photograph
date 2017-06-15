# CR: consider giving this file a better name. what's its purpose?
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

    db = client['net_photographs']

    simulation = db.simulation

    #emotions.insert_many(SEED_DATA)  # CR: one space after `#`

    query = {'id': 1}

    
    #simulation.update(query, {'$set': {'lightPower': 1}})

    cursor = simulation.find({'id': 1})
    
    #print(cursor)
    
    for doc in cursor:
        print(doc['id'], doc['faceTime'], doc['lightPower'], doc['prevLightPower'], doc['faces'], doc['prevFaces'])

    #db.drop_collection('emotions')
    client.close()

if __name__ == '__main__':
    main()
