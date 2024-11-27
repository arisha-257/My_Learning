import redis


# Connect to Redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
print(r.ping()) 
# Set and get a key
# r.set("name", "Alice")
print(r.get("name"))
