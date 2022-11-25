import pymongo
from pymongo import MongoClient
import pandas as pd
from pandas import DataFrame
import time
from bson.json_util import dumps
import os
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time


## This file creates a live graph that updates in real-time data that is written to the heartData collection

uri = "mongodb+srv://genial:admin@subarcticmonkeys.geqfqed.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client['arcticChallenge']
coll = db['heartData']
x = []
y = []
index = count()

fig = plt.figure(figsize=(15, 7))
ax = fig.add_subplot()
plt.style.use('fivethirtyeight')

def animate(i, x, y):
    current_time = time.time() 

    t = time.time()
    cursor = coll.find({"timestamp" : { "$lt": t }})
    x_val = [float(c["timestamp"]) for c in cursor]
    cursor = coll.find({"timestamp" : { "$lt": t }})

    y_val = []
    for c  in cursor:
        try:
            y_val.append([float(c["value"])])
        except ValueError as e:
            print(e)
  #  x.extend(x_val)
   # y.extend(y_val)

     # Limit x and y lists to 20 items
    x = x_val
    y = y_val
    x = x[-20:]
    y = y[-20:]

     # Draw x and y lists
    ax.clear()
    ax.plot(x, y)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('heartData vs Time')
    plt.ylabel('heartData')
    plt.xlabel('Timstamp (Msecs)')

    

ani = FuncAnimation(plt.gcf(), animate,  fargs=(x,y), interval=100)

plt.show()