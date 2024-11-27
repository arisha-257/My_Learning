from pymongo import MongoClient
from datetime import datetime, timezone

MONGODB_URI = "mongodb+srv://admin:admin@cluster0.wsrz0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGODB_URI)

# this line will retuen all the database name

# for db_name in client.list_database_names():
#     print(db_name)

db = client.bank
# Get reference to 'accounts' collection
accounts_collection = db.accounts

new_account = {
    "account_holder": "Linus Torvalds",
    "account_id": "MDB829001337",
    "account_type": "checking",
    "balance": 50352434,
    "last_updated": datetime.now(timezone.utc),
}

# Write an expression that inserts the 'new_account' document into the 'accounts' collection.
# result = accounts_collection.insert_one(new_account)

# document_id = result.inserted_id
# print(f"_id of inserted document: {document_id}")

# inserted_document = accounts_collection.find_one({"account_id": "MDB829001337"})
# print("Inserted Document:", inserted_document)

new_accounts = [
    {
        "account_id": "MDB011235813",
        "account_holder": "Ada Lovelace",
        "account_type": "checking",
        "balance": 60218,
    },
    {
        "account_id": "MDB829000001",
        "account_holder": "Muhammad ibn Musa al-Khwarizmi",
        "account_type": "savings",
        "balance": 267914296,
    },
]

# Write an expression that inserts the documents in 'new_accounts' into the 'accounts' collection.
result = accounts_collection.insert_many(new_accounts)

document_ids = result.inserted_ids
print("is data inserted successfully :", result.acknowledged)
print("# of documents inserted: " + str(len(document_ids)))
print(f"_ids of inserted documents: {document_ids}")


client.close()
