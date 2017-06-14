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

    emotions = db.emotions

    #emotions.insert_many(SEED_DATA)

    query = {'id': 1}

    
    emotions.update(query, {'$set': {'name': 'success'}})

    cursor = emotions.find({'id': 1})
    
    print(cursor)
    
    for doc in cursor:
        print ('there was %s in id: %s and measure is %s ' %
               (doc['name'], doc['id'], doc['measure']))

    db.drop_collection('emotions')
    client.close()


main()
