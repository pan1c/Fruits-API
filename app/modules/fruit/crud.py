"""
Data-access helpers that encapsulate SQLAlchemy queries.
Keeping them separate from routers makes unit-testing easier.
"""

from typing import Optional, Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.fruit.models import Fruit
from app.modules.fruit.schemas import FruitIn


async def create_fruit(db: AsyncSession, data: FruitIn) -> Fruit:
    new_fruit = Fruit(**data.model_dump())
    db.add(new_fruit)
    await db.commit()
    await db.refresh(new_fruit)
    return new_fruit


async def get_fruit(db: AsyncSession, fruit_id: int) -> Optional[Fruit]:
    res = await db.execute(select(Fruit).where(Fruit.id == fruit_id))
    return res.scalar_one_or_none()


async def list_fruits(db: AsyncSession) -> Sequence[Fruit]:
    res = await db.execute(select(Fruit))
    return res.scalars().all()
