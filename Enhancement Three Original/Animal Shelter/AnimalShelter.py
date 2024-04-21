from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter (object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, USER, PASS):
        #Initializing the MongoClient. This helps to
        #access the MongoDB databases and collections.
        #This is hard-wired to use the aac database, the
        #animals collection, and the aac user.
        #Definitions of the connection string variables are
        #unique to the individual Apporto environment.
        #
        #You must edit the connection variables below to reflect
        #your own instance of MongoDB!
        #
        #Connection Variables
        #
        USER = 'aacuser'
        PASS = 'Penguins1'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30449
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@localhost:30449/test?authSource=AAC'%("aacuser", "aacuser"))
        self.database = self.client['AAC']
        self.collection = self.database['animals']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            result = self.database.animals.insert_one(data)
            if insert!=0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, criteria=None):
        if criteria is not None:
            data = self.database.animals.find(criteria,{"_id": False})
            for document in data:
                print(document)
        else:
            data = self.database.animals.find({}, {"_id": False})
            
        return data
    