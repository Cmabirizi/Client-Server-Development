from pymongo import MongoClient
from pymongo.errors import PyMongoError

class AnimalShelter:
    def __init__(self, username, password, host='localhost', port=27017):
        self.client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}/aac')
        self.database = self.client['aac']
        self.collection = self.database['animals']

    def create(self, data):
        try:
            if data is not None:
                self.collection.insert_one(data)
                return True
            return False
        except PyMongoError as e:
            print(f"Create Error: {e}")
            return False

    def read(self, criteria):
        try:
            return list(self.collection.find(criteria))
        except PyMongoError as e:
            print(f"Read Error: {e}")
            return []

    def update(self, criteria, new_data):
        try:
            result = self.collection.update_many(criteria, {'$set': new_data})
            return result.modified_count
        except PyMongoError as e:
            print(f"Update Error: {e}")
            return 0

    def delete(self, criteria):
        try:
            result = self.collection.delete_many(criteria)
            return result.deleted_count
        except PyMongoError as e:
            print(f"Delete Error: {e}")
            return 0