from http import client
import pymongo
import json
from pymongo import MongoClient, InsertOne

class ScriptsMongoDB:
    def __init__(self) -> None:

        super().__init__()

        self.client = pymongo.MongoClient("mongodb+srv://alfa2bd:<password>@clusteralfa2bd.tirlce4.mongodb.net/?retryWrites=true&w=majority")

        self.db = self.client.BaseAlfa2

        self.collection = self.db.gestores

    def send_json_to_db(self, *args, **kwargs)->None:

        if 'path_json' in kwargs:

            path_json = kwargs['path_json']

            requesting = []

            with open(path_json) as json_file:
                data_dict = json.load(json_file)
                requesting.append(InsertOne(data_dict))

            result = self.collection.bulk_write(requesting)

    def close_connection(self):
        self.client.close()
