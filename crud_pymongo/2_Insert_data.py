import pymongo
client = pymongo.MongoClient("mongodb://localhost/27017")
print(client)
db=client['gaurav']
collection =db['teacher_Info']

#Insert many
data=[{"name":"snajay bhakkad","sub":"python","id":4},
      {"name":"sangita phunde","sub":"adbms","id":7},
      {"name":"udayharry nagarkar","sub":"spm","id":1}
      ]

collection.insert_many(data)
print("done!")
