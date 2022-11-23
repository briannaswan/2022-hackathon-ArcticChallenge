import json
import pymongo
from pymongo import MongoClient
import pandas as pd

# Needed for the change streams
import os
from bson.json_util import dumps

# Needed for reading the data from the Arduino
import time
import datetime

import serial
import serial.tools.list_ports

# Create a new empty collection in the database
def createCollection(URI, db_name, collection_name):
    """ Creates an empty collection in a specified database.
    """
    client = MongoClient(URI)
    db = client[db_name]

    if collection_name in db.list_collection_names():
        print("\nThis collection already exists.")
    else:
        print("This collection does not exist.")
        db.create_collection(collection_name)
        print("Collection has been created.")


def deleteCollection(URI, db_name, collection_name):
    """ Deletes a collection and all of its contents.
    """
    client = MongoClient(URI)
    db = client[db_name]

    if collection_name in db.list_collection_names():
        print("This collection  exists.\n")
        db.drop_collection(collection_name)
        print("Collection has been deleted.")
    else:
        print("This collection does not exist.")

#  Parse a CSV, convert to JSON, and upload to a collection in the database
def importCSV(URI, csv_path, db_name, collection_name):
    """ Imports a csv file at path csv_name to a mongo colection
    returns: count of the documants in the collection
    """

    client = MongoClient(URI)
    db = client[db_name]
    coll = db[collection_name]

    # Read the csv to pandas
    data = pd.read_csv(csv_path)

    # convert to json
    data_json = json.loads(data.to_json(orient='records'))
    coll.insert_many(data_json)
    return print("Number results in collection", collection_name, ":", coll.count_documents({}) )

def watchCollection(URI, db_name, collection_name):
    """ Uses a change stream to watch for changes in a specified database collection
    """
    client = MongoClient(URI)
    db = client[db_name]
    coll = db[collection_name]
    ("Current number of entries in ",collection_name," : " , coll.count_documents({}))

    change_stream = coll.watch()
    for change in change_stream:
        print(dumps(change))
        print("Data overwritten. New number of entries:" , coll.count_documents({}))
        print('') # for readability
         
def writeArduinoData(URI, db_name, collection_name, serial_port, baud_rate):
    """ Taking data from an Arduino connected via the Serial Port to a PC (USB), writes to a specified collection in the database.
    """
    client = MongoClient(URI)
    db = client[db_name]
    coll = db[collection_name]
    print("Current number of entries in ",collection_name," : " , coll.count_documents({}))

    time.sleep(0.001)

    # set up the serial line
    s_port = serial_port
    b_rate = baud_rate

    ser = serial.Serial(s_port, b_rate)
    start_time = datetime.datetime.now()

    while True:
        line = ser.readline()
        end_time = datetime.datetime.now()
        time_diff = (end_time - start_time)
        execution_time = time_diff.total_seconds() * 1000

        n = line.decode().strip().split(",")[0]
        json = {"value": n, "Msec" : execution_time}
        coll.insert_one(json)
        print(json)
        time.sleep(0.05)




