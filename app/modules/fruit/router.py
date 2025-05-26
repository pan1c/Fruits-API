"""
HTTP endpoints for the Fruit resource.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_db
from app.modules.fruit import crud, schemas

router = APIRouter()


@router.get("/fruits", response_model=list[schemas.FruitOut])
async def read_fruits(db: AsyncSession = Depends(get_db)):
    """Return all fruits."""
    # Fetch all fruits from the database
    return await crud.list_fruits(db)


@router.get(
    "/fruits/{fruit_id}",
    response_model=schemas.FruitOut,
    responses={404: {"description": "Fruit not found"}},
)
async def read_fruit(fruit_id: int, db: AsyncSession = Depends(get_db)):
    """Return a single fruit by ID."""
    # Fetch a fruit by its ID or raise 404 if not found
    fruit = await crud.get_fruit(db, fruit_id)
    if fruit is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Fruit not found"
        )
    return fruit


@router.post(
    "/fruits",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.FruitOut,
)
async def create_fruit(fruit_in: schemas.FruitIn, db: AsyncSession = Depends(get_db)):
    """Add a new fruit and return it with its generated ID."""
    # Create a new fruit in the database
    return await crud.create_fruit(db, fruit_in)
