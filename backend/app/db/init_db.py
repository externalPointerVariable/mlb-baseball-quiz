import asyncio
import logging
from app.core.database import engine, Base

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

async def init_db():
    """
    Initializes the database by creating all tables defined in the ORM models.
    """
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.info("✅ Database initialized successfully")
    except Exception as e:
        logger.error("❌ Failed to initialize the database", exc_info=True)

if __name__ == "__main__":
    asyncio.run(init_db())
