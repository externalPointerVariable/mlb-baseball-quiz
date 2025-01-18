# Initializes the database by creating necessary tables

import asyncio
from db import async_engine, base

async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(init_db())
