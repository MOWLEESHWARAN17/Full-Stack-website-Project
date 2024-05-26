from motor.motor_asyncio import AsyncIOMotorClient
from model import create_user_index

MONGO_DETAILS = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_DETAILS)

database = client.my_fastapi_app

# Ensure indexes are created
async def init_db():
    await create_user_index(database)

def get_database():
    return database
