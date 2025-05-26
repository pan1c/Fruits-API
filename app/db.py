import logging
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app import config

logger = logging.getLogger(__name__)

# Create an async engine using the database URL from config
engine = create_async_engine(config.DATABASE_URL, echo=False)

# Create an async session factory
SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)


# Base class for all ORM models
class Base(DeclarativeBase):
    pass


# Dependency to get a database session for each request
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session


# Initialize the database and create tables
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        logger.info("Database initialized successfully")
