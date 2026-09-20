from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings


class Database:
    client = None
    db = None


db_instance = Database()


async def connect_to_mongo():
    try:
        client = AsyncIOMotorClient(
            settings.MONGODB_URL,
            serverSelectionTimeoutMS=5000,
            connectTimeoutMS=5000,
        )

        # Confirm that the configured database is reachable.
        await client.admin.command("ping")

        db_instance.client = client
        db_instance.db = client[settings.DATABASE_NAME]

        # Do not print MONGODB_URL because it can contain credentials.
        print(f"Connected to MongoDB database: {settings.DATABASE_NAME}")

    except Exception as exc:
        db_instance.client = None
        db_instance.db = None
        print(f"MongoDB unavailable; in-memory mode active: {exc}")
        return

    try:
        await db_instance.db["users"].create_index("email", unique=True)
        await db_instance.db["villages"].create_index("village_id", unique=True)
        await db_instance.db["businesses"].create_index(
            "business_id", unique=True
        )
        await db_instance.db["business_models"].create_index(
            "category", unique=True
        )
        await db_instance.db["village_business_stats"].create_index(
            [("village_id", 1), ("category", 1)],
            unique=True,
        )
        await db_instance.db["legal_offices"].create_index(
            "office_id", unique=True
        )
        await db_instance.db["schemes"].create_index(
            "scheme_id", unique=True
        )
    except Exception as exc:
        # The database remains usable even if an index already conflicts.
        print(f"MongoDB index creation skipped: {exc}")


async def close_mongo_connection():
    if db_instance.client is not None:
        db_instance.client.close()
        db_instance.client = None
        db_instance.db = None
        print("Closed MongoDB connection")


def get_database():
    return db_instance.db