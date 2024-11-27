from pymongo import MongoClient
from pprint import pprint


MONGODB_URI = "mongodb+srv://admin:admin@cluster0.wsrz0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGODB_URI)

# this line will return all the database name

# for db_name in client.list_database_names():
#     print(db_name)


# Get reference to 'bank' database
db = client.bank

# Get a reference to the 'accounts' collection
accounts_collection = db.accounts

# Calculate the average balance of checking and savings accounts with balances of less than $60418.
select_by_balance = {"$match": {"balance": {"$gt": 60418}}}


# Separate documents by account type and calculate the average balance for each account type.
separate_by_Account_calculate_avg_value = {
    "$group": {"_id": "$account_type", "avg_balance": {"$avg": "$balance"}}
}
pipeline = [select_by_balance, separate_by_Account_calculate_avg_value]
results = accounts_collection.aggregate(pipeline)


print()
print(
    "Average balance of checking and savings accounts with balances of less than $1000:",
    "\n",
)

for item in results:
    pprint(item)
client.close()
