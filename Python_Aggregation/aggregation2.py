from pymongo import MongoClient
from pprint import pprint


MONGODB_URI = "mongodb+srv://admin:admin@cluster0.wsrz0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGODB_URI)


# Get reference to 'bank' database
db = client.bank

# Get a reference to the 'accounts' collection
accounts_collection = db.accounts

# Return the account type, original balance, and balance converted to Great British Pounds (GBP)
# of all checking accounts with an original balance of greater than $1,500 US dollars, in order from highest original balance to lowest.

# To calculate the balance in GBP, divide the original balance by the conversion rate
conversion_rate_usd_to_gbp = 1.3

# Select checking accounts with balances of more than $1,500.
select_accounts = {"$match": {"account_type": "checking", "balance": {"$gt": 1500}}}

# Organize documents in order from highest balance to lowest.
organize_by_original_balance = {"$sort": {"balance": -1}}

# Return only the account type & balance fields, plus a new field containing balance in Great British Pounds (GBP).
# this ths projection
return_specified_fields = {
    "$project": {
        "account_type": 1,
        "balance": 1,
        "account_id": 1,
        "gbp_balance": {"$divide": ["$balance", conversion_rate_usd_to_gbp]},
        "_id": 0,
    }
}

# Create an aggegation pipeline containing the four stages created above
pipeline = [
    select_accounts,
    organize_by_original_balance,
    return_specified_fields,
]

# Perform an aggregation on 'pipeline'.
results = accounts_collection.aggregate(pipeline)

print(
    "Account type, original balance and balance in GDP of checking accounts with original balance greater than $1,500,"
    "in order from highest original balance to lowest: ",
    "\n",
)

for item in results:
    pprint(item)
    print()

client.close()
