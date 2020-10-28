from pymongo import MongoClient


class Connection:
    def __init__(self, connection_string):
        self.db = MongoClient(connection_string)['users-db']


db = Connection('mongodb+srv://alifilho:aomc020702@users-db.jmdmt.mongodb.net/users-db?retryWrites=true&w=majority').db
