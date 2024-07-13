from pymongo import MongoClient
from pymongo.server_api import ServerApi

def get_mongodb():
    uri = "mongodb+srv://rezvaserg:FdhiHDdmAphGFbzg@cluster0.5izpshs.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        # print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    db = client["GoIT8"]

    return db
    