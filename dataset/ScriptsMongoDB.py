import pymongo
import json
from pymongo import MongoClient, InsertOne
from dotenv import load_dotenv
import os

class ScriptsMongoDB:
    def __init__(self) -> None:

        super().__init__()

        load_dotenv()

        user = os.getenv('DB_MONGO_USER')
        password = os.getenv('DB_MONGO_PASSWORD')
        dbname = os.getenv('DB_MONGO_NAME')
        cluster_name = os.getenv('DB_MONGO_CLUSTER')

        self.client = MongoClient("mongodb+srv://{}:{}@{}.tirlce4.mongodb.net/?retryWrites=true&w=majority".format(
            user,
            password,
            dbname,
            cluster_name
        ))

        self.db = self.client[dbname]

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
