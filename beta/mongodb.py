import sys
import pymongo

SEED_DATA = [
    {
        'id': 1,
        'name': 'try',
        'measure': 5,
    },
    {
        'id': 2,
        'name': 'try2',
        'measure': 10,
    },
    {
        'id': 3,
        'name': 'try3',
        'measure': 15,
    }
    ]
    uri = 'mongodb://net_photo:net.photo456@ds111771.mlab.com:11771/net_photographs'

    def main(args):

    client = pymongo.MongoClient(uri)

    db = client.get_default_database()

    photos = db['photos']

    photos.insert_many(SEED_DATA)

    query = {'id': 1}

    photos.update(query, {'$set': {'name': 'success'}})

    cursor = photos.find({'name': {'success'}}).sort('id', 1)

    for doc in cursor:
        print ('In the %s, %s by %s topped the charts for %d straight weeks.' %
               (doc['decade'], doc['song'], doc['artist'], doc['weeksAtOne']))

    #db.drop_collection('songs')
    #db.drop_collection('songs')
    if __name__ == '__main__':
    main(sys.argv[1:])
