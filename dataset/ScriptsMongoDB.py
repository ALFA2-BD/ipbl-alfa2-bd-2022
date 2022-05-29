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
        cluster_name = os.getenv('DB_MONGO_CLUSTER')

        dbname = os.getenv('DB_MONGO_NAME')

        self.client = MongoClient("mongodb+srv://{}:{}@{}.tirlce4.mongodb.net/?retryWrites=true&w=majority".format(
            user,
            password,
            dbname,
            cluster_name
        ))

        self.db = self.client[dbname]

    def send_json_to_db(self, *args, **kwargs)->None:

        if 'path_json' in kwargs and 'collection_name' in kwargs:

            path_json = kwargs['path_json']
            collection_name = kwargs['collection_name']

            collection = self.db[collection_name]

            requesting = []

            with open(path_json) as json_file:
                list_dict = json.load(json_file)
                for data_dict in list_dict:
                    requesting.append(InsertOne(data_dict))

            try:
                collection.bulk_write(requesting)
            except Exception as e:
                print(e)

    def delete_elements_from_collection(self, *args, **kwargs):

        if 'collection_name' in kwargs:

            collection_name = kwargs['collection_name']
            collection = self.db[collection_name]

            collection.remove()

    def create_collection(self, *args, **kwargs):

        if 'collection_name' in kwargs:

            collection_name = kwargs['collection_name']
            _ = self.db[collection_name]

    def list_collections(self, *args, **kwargs):

        return self.db.list_collection_names()

    def verify_collection_in_db(self, *args, **kwargs):

        if 'collection_name' in kwargs:

            collection_name = kwargs['collection_name']
            list_of_collection = self.list_collections()

            return collection_name in list_of_collection

        return False

    def close_connection(self, *args, **kwargs):

        self.client.close()
