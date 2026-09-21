import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings


async def main():
    print("Testing MongoDB...")

    client = AsyncIOMotorClient(
        settings.MONGODB_URL,
        serverSelectionTimeoutMS=10000,
        connectTimeoutMS=10000,
    )

    try:
        result = await client.admin.command("ping")
        print("MongoDB PING:", result)
        print("✅ MongoDB connection successful!")

    except Exception as e:
        print("❌ MongoDB connection failed:")
        print(e)

    finally:
        client.close()


asyncio.run(main())
