from pymongo import MongoClient
from pprint import pprint
from bson.objectid import ObjectId


MONGODB_URI = "mongodb+srv://admin:admin@cluster0.wsrz0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGODB_URI)

# Get reference to 'bank' database
db = client.bank

# Get a reference to the 'accounts' collection
accounts_collection = db.accounts

# Query by ObjectId
document_to_find = {"_id": ObjectId("673ef37f377fd1f7cd1f16ba")}

# Write an expression that retrieves the document matching the query constraint in the 'accounts' collection.
result = accounts_collection.find_one(document_to_find)

# Query
documents_to_find = {"balance": {"$gt": 4700}}

# Write an expression that selects the documents matching the query constraint in the 'accounts' collection.
cursor = accounts_collection.find(documents_to_find).explain()
# pprint(result)

num_docs = 0
for document in cursor:
    num_docs += 1
    pprint(document)
    print()
print("# of documents found: " + str(num_docs))

client.close()
