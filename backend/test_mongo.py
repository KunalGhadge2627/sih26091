import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

uri = os.getenv("MONGODB_URI")

print("URI exists:", bool(uri))

try:
    client = MongoClient(
        uri,
        serverSelectionTimeoutMS=10000,
        connectTimeoutMS=10000,
        tls=True,
    )

    print(client.admin.command("ping"))
    print("MongoDB Atlas connection successful!")

except Exception as e:
    print("MongoDB connection failed:")
    print(repr(e))