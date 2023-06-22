import  pymongo
from pymongo import MongoClient

# creation of MongoClient
client=MongoClient()

# Connect with the portnumber and host
client = MongoClient('mongodb://localhost:27017/')

# Access database
mydatabase = client["python"]

# Access collection of the database
mycollection=mydatabase["dbconnect"]

# dictionary to be added in the database
rec=[{
    "_id":"2",
    "name":"Gaurav",
    "age":21

}]

# inserting the data in the database
rec = mydatabase.dbconnect.insert(rec)
