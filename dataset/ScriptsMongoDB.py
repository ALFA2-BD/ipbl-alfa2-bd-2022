from http import client
import pymongo
import json
from pymongo import MongoClient, InsertOne
from bson import json_util

class ScriptsMongoDB:
    def __init__(self) -> None:

        super().__init__()

        self.client = pymongo.MongoClient("mongodb+srv://alfa2bd:alfa2bd@clusteralfa2bd.tirlce4.mongodb.net/?retryWrites=true&w=majority")

        self.db = self.client.BaseAlfa2

        self.collection = self.db.gestores

    def send_json_to_db(self, *args, **kwargs)->None:

        if 'path_json' in kwargs:

            path_json = kwargs['path_json']

            requesting = []

            with open(path_json) as json_file:
                list_dict = json.load(json_file)
                for data_dict in list_dict:
                    requesting.append(InsertOne(data_dict))

            try:
                result = self.collection.bulk_write(requesting)
            except Exception as e:
                print(e)

    def close_connection(self):
        self.client.close()
