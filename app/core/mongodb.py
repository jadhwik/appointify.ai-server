from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from app.core.config import settings
from typing import Optional

class MongoDB:
    client: Optional[AsyncIOMotorClient] = None
    
mongodb = MongoDB()

async def connect_to_mongo():
    """Connect to MongoDB on startup"""
    mongodb.client = AsyncIOMotorClient(settings.MONGODB_URL)
    print("✅ Connected to MongoDB")

async def close_mongo_connection():
    """Close MongoDB connection on shutdown"""
    if mongodb.client:
        mongodb.client.close()
        print("❌ Closed MongoDB connection")

def get_database():
    """Get MongoDB database instance"""
    return mongodb.client[settings.MONGODB_DB_NAME]

async def get_mongo_db():
    """Dependency to get MongoDB database"""
    return get_database()