'''
Loading data to MongoDB
'''

import pandas as pd
import pymongo
import json
from dotenv import load_dotenv
from mushroom.config import mongo_client
from mushroom.logger import logging


DATA_FILE_PATH = "/config/workspace/mushrooms.csv"
DATABASE_NAME = "mushroom_classification"
COLLECTION_NAME = "mushroom"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(df.head())
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
