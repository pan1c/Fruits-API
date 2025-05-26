"""
SQLAlchemy ORM model for the `fruit` table.
"""

from sqlalchemy import Column, Integer, String

from app.db import Base


class Fruit(Base):
    # SQLAlchemy model representing a fruit entity with its name and color.
    """Represents a fruit with its name and color attributes."""
    __tablename__ = "fruit"

    id = Column(Integer, primary_key=True, index=True)
    fruit = Column(String(length=50), nullable=False)
    color = Column(String(length=30), nullable=False)
