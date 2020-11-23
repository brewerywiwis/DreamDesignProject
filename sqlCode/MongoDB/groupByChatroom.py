from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://admin:1234@34.87.125.21:27017/?authSource=dreamdesignDB&readPreference=primary&appname=MongoDB%20Compass&ssl=false')
result = client['dreamdesignDB']['Message'].aggregate([
    {
        '$group': {
            '_id': '$rid', 
            'messageSender': {
                '$push': {
                    'sender': '$uid', 
                    'message': '$message', 
                    'time': '$time', 
                    'picture': '$picture'
                }
            }
        }
    }, {
        '$sort': {
            'time': 1
        }
    }
])