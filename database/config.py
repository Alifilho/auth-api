from pymongo import MongoClient


class Connection:
    def __init__(self, connection_string):
        self.db = MongoClient(connection_string)['users-db']


db = Connection('mongodb+srv://<user>:<password>@<db>.jmdmt.mongodb.net/<db>?retryWrites=true&w=majority').db
