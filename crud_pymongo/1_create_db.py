import pymongo

client1 =pymongo.MongoClient("mongodb://localhost:27017")
print(client1)
db = client1['gaurav']



collection =db['student_info']
data={'name':'vaibhav','no':2,"add":'Kolgaon'}
collection.insert_one(data)
print("data insert successfully.")