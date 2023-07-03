import pymongo

# Connect with the portnumber and host
client = pymongo.MongoClient('mongodb://localhost:27017/')

# Access database
db = client["demo_table"]

# Access collection of the database
mycol=db["demo"]

# dictionary to be added in the database
mydict=[{"name":"vishal", "age":21},
    {"name":"gaurav","rollNO":48}
]

# inserting the data in the database
x = mycol.dbconnect.insert_many(mydict)
print(x)
print("done")