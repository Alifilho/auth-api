from pymongo import ReturnDocument

from database.config import db
from bson import ObjectId


class UserService:
    def __init__(self):
        self.users = db['users']

    def save_sync(self, user):
        return self.users.insert_one(user)

    def delete_sync(self, user_id):
        return self.users.find_one_and_delete({'_id': ObjectId(user_id)})

    def get_all_sync(self):
        return self.users.find()

    def update_sync(self, user_id, updates):
        return self.users.find_one_and_update({'_id': ObjectId(user_id)}, {'$set': updates},
                                              return_document=ReturnDocument.AFTER)
