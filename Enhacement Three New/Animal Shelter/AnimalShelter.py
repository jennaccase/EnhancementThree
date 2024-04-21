from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps

class AnimalShelter (object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, username, password):
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
        username = 'aacuser'
        password = 'Penguins1'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30449
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@localhost:30449/test?authSource=AAC' % ("aacuser", "aacuser"))
        self.database = self.client["AAC"]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)
            if insert!=0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

#Inserts multiple files into database
    def insertMany(self, data: dict):
        if data is not None and type(data) is dict:
            try:
                self.database.animals.insert_many(data)
                return True
            except Exception as e:
                print("An exception has occured ::", e)
            return False
        else:
            raise Exception("Nothing to save, because parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, criteria=None):
        if criteria is not None:
            data = self.database.animals.find(criteria,{"_id": False})
            for document in data:
                print(document)
        else:
            data = self.database.animals.find({}, {"_id": False})
            
        return data

#Create method to implement the U in CRUD
    def update(self, initial, change):
        if initial is not None:
            if self.database.animals.count_documents(initial, limit = 1) != 0:
                update_result = self.database.animals.update_many(initial, {"$set": change})
                result = update_result.raw_result
            else:
                result = "No document found"
            return result
        else:
            raise Exception("Nothing to update beacsue data parameter is empty")

#Update multiple files at once
    def updateMany(self, query: dict, changes: dict) -> str:
        if (query is not None and type(query) is dict) and (changes is not None and type(changes) is dict):
            updated = self.database.animals.update_many(query, changes)
            return dumps(updated.raw_results)
        else:
            raise Exception("Update error: invalid update parameters")

#Create method to implement the D in CRUD
    def delete(self, remove):
        if remove is not None:
            if self.database.animals.count_documents(remove, limit = 1) != 0:
                delete_result = self.database.animals.delete_many(remove)
                result = delete_result.raw_result
            else:
                result = "No document found"
            return result
        else:
            raise Exception("Nothing to delete because data parameter is empty")

#Delete multiple files at once
     def deleteMany(self, remove: dict) -> str:
        """Delete a document from the AAC database"""
        if remove is not None and type(remove) is dict:
            deleted = self.database.animals.delete_many(remove)  
            return dumps(deleted.raw_result)  
        else:
            raise Exception("Delete error: invalid delete parameter")