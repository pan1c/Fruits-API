# Unit tests for the FruitIn schema

import pytest
from pydantic import ValidationError

from app.modules.fruit.schemas import FruitIn


# Test that FruitIn schema accepts valid data
def test_fruit_schema_validation():
    data = {"fruit": "mango", "color": "orange"}
    fruit = FruitIn(**data)
    assert fruit.fruit == "mango"
    assert fruit.color == "orange"


# Test that FruitIn schema raises ValidationError for invalid color
def test_fruit_schema_invalid_color():
    data = {"fruit": "mango", "color": None}
    with pytest.raises(ValidationError) as exc_info:
        FruitIn(**data)

    # Optional: assert specific error message
    errors = str(exc_info.value)
    assert (
        "Input should be a valid string" in errors
    )  # Check error message for invalid string
    assert "color" in errors  # Ensure 'color' field is mentioned in the error
