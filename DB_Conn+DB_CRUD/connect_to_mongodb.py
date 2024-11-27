from pymongo import MongoClient


MONGODB_URI = "mongodb+srv://admin:admin@cluster0.wsrz0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGODB_URI)

# this line will retuen all the database name

for db_name in client.list_database_names():
    print(db_name)


client.close()
