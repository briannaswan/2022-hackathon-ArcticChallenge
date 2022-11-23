import subarctic

path = "data/example_data.csv"
db = "arcticChallenge"
coll ="test_collection"
uri = "mongodb+srv://genial:admin@subarcticmonkeys.geqfqed.mongodb.net/?retryWrites=true&w=majority"

## Create a new collection with nothing in it
subarctic.createCollection(uri, db, "test_collection")
## Load CSV data to the new collection
subarctic.importCSV(uri, path, db, coll)


### Uncomment out the following if you want to watch for changes in a specified collection
###  Watch for changes in heartData, the Arduino needs to be connnected: 
# watch_collection = 'heartData'
# subarctic.watchCollection(uri, db, watch_collection)
