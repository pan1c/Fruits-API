"""
Central place for runtime configuration.
"""

import os

# Optional with defaults
ENV = os.getenv("ENV", "dev").lower()
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
SQL_LOG_LEVEL = os.getenv("SQL_LOG_LEVEL", "WARNING").upper()
DATABASE_URL = os.getenv("DATABASE_URL")


def validate_env() -> None:
    """Validate required environment variables."""
    if not DATABASE_URL:
        raise ValueError(
            "Missing required environment variable: DATABASE_URL. "
            "Please set DATABASE_URL in your environment or .env file, for example: "
            "DATABASE_URL='postgresql+asyncpg://user:pass@localhost:5432/dbname'"
        )


validate_env()
