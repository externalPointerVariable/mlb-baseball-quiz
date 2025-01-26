from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from app.core.config import settings

class Base(DeclarativeBase):
    pass

engine = create_async_engine(
    settings.DATABASE_URL,
    future=True,
    echo=True
)

async_session = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

class Base(DeclarativeBase):
    pass

async def load_achievements(session: AsyncSession):
    async with async_session() as session:
        yield session
