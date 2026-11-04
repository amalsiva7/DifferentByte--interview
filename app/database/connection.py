from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
)
from app.core.config import settings


# 1. Create the database engine
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,
)


# 2. Create a session factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


# 3. Database dependency for FastAPI
async def get_db():
    async with AsyncSessionLocal() as db:
        yield db
