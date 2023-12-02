from src.models.base import Base, engine


async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
