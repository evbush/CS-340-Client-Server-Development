from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint
from bson.json_util import dumps


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, un, pw):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.       
        self.client = MongoClient('mongodb://%s:%s@localhost:29836/?authSource=AAC' % (un, pw))
        # where xxxx is your unique port number
        self.database = self.client['AAC']

# CREATE Method
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary
            print('True')
        else:
            raise Exception('False..nothing to save, because data parameter is empty')

# READ Method
    def read(self, data):
        if data is not None:
            return list(self.database.animals.find(data, {"_id": False}))
        else:
            print("Error: no query present")
            
# UPDATE Method
    def update(self, search, field, value):
        filter = { 'animal_id': search }
        replace = { '$set': { field: value } }

        if filter is not None:
            self.database.animals.update_one(filter, replace)

            cursor = self.database.animals.find( {'animal_id': 'A875947' })
            for record in cursor:
                pprint(record)
        else:
            raise Exception("Error...object not found")

# DELETE Method
    def delete(self, search):
        filter = { 'animal_id': search }
        
        if filter is not None:
            delete = self.database.animals.delete_many(filter)
            print(delete.deleted_count, 'document(s) deleted...')
            pprint(delete)
        else:
            print('Error...object not found')
            
        
        
        
        
            