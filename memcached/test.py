import memcache

client = memcache.Client(["localhost:11211"])

client.set("your_key", "your_value")
value = client.get("your_key")
print(value)
