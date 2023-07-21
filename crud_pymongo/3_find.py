import pymongo
client = pymongo.MongoClient("mongodb://localhost/27017")
print(client)
db=client['gaurav']
collections =db['teacher_Info']
# one =collections.find_one()
# one = collections.find_one({ "id":1})
two = collections.find({"id":1})
for i in two:
    print(i)