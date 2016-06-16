#!/usr/bin/env python
# import sys
# import pandas as pd
# import pymongo
# import json
# import os
#
# def import_content(filepath):
#     mng_client = pymongo.MongoClient('mongodb://huong:123456@ds025973.mlab.com:25973/data_kcal')
#     mng_db = mng_client.get_default_database() # Replace mongo db name
#     collection_name = 'kcal' # Replace mongo db collection name
#
#     db_cm = mng_db[collection_name]
#     cdir = os.path.dirname(__file__)
#     file_res = os.path.join(cdir, filepath)
#
#     data = pd.read_csv(file_res)
#     data_json = json.loads(data.to_json(orient='records'))
#     db_cm.remove()
#     db_cm.insert(data_json)
#
# if __name__ == "__main__":
#   filepath = 'D:/ABBREV.csv'  # pass csv file path
#   import_content(filepath)

import pymongo
db_uri = "mongodb://huong:123456@ds025973.mlab.com:25973/data_kcal"

db = pymongo.MongoClient(db_uri).get_default_database()
kcal_collection = db['kcal']

n = str(input("Enter your food: "))
def collect_choice(x):
    data_find = kcal_collection.find({'Food': x})
    l = []
    for i in data_find:
        l.append(i['short'])
    return l

nz = str(input("Enter your choice: "))
for i in l:



