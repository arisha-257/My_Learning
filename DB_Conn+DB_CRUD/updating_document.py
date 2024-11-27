from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint


MONGODB_URI = "mongodb+srv://admin:admin@cluster0.wsrz0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGODB_URI)

db = client.bank
# Get reference to 'accounts' collection
accounts_collection = db.accounts

# Filter
document_to_update = {"_id": ObjectId("673ef37f377fd1f7cd1f16ba")}

# Update
add_to_balance = {"$inc": {"balance": 100}}

# Print original document
# pprint(accounts_collection.find_one(document_to_update))

# Write an expression that adds to the target account balance by the specified amount.
# result = accounts_collection.update_one(document_to_update, add_to_balance)
# print("Documents updated: " + str(result.modified_count))


# print("---------------------update Document-----------------------")
# Print updated document
# pprint(accounts_collection.find_one(document_to_update))

# Filter
select_accounts = {"account_type": "savings"}

# Update
set_field = {"$set": {"minimum_balance": 100}}

# Write an expression that adds a 'minimum_balance' field to each savings acccount and sets its value to 100.
result = accounts_collection.update_many(select_accounts, set_field)

print("Documents matched: " + str(result.matched_count))
print("Documents updated: " + str(result.modified_count))
pprint(accounts_collection.find_one(select_accounts))


client.close()
