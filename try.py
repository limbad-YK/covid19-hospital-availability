import pymongo

mongo = pymongo.MongoClient(
        host = "localhost",
        port = 27017,
        serverSelectionTimeoutMS = 1000
    )
db = mongo.company
mongo.server_info()

for x in db.users.find({},{"email":"hello1@gmail.com","pass":"12345"}):
    print(x)