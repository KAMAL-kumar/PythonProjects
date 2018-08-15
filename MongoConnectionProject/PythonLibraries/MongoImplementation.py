import pymongo
import pprint
from pymongo import MongoClient

templateString = "Customer Name: "

client = MongoClient()

#Get the databases in the DB

db = client.mycustomers

#Get the collection

customerRecords = db.customers

#print the count of the records

print(customerRecords.estimated_document_count())

# #print all the existing records

# print("Existing customers:")
# for record in customerRecords.find():
# 	pprint.pprint(templateString + record["first_name"])

# #create the new record

# newRecord = {
# 	"first_name":"Jaya",
# 	"last_name" : "Bachan",
# 	"age":50,
# 	"role":"Mahanayaki",
# 	"address":{
# 		"city":"Mumbai",
# 		"locality":"Warli C Link",
# 		"street_no":1
# 	},
# 	"customerId":7
# }

# #insert the new record

# isnertedObjectId = customerRecords.insert_one(newRecord).inserted_id

# #get the inserted record and print it

# insertedRecord = customerRecords.find_one({"_id":isnertedObjectId})

# print("Inserted customer is:")

# pprint.pprint(insertedRecord)




