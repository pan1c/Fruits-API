# app/logger.py
import logging

from app import config


def setup_logging() -> None:
    """
    Configure root logger and route Uvicorn logs through it.
    Call this once, ideally at application startup.
    """
    fmt = "%(asctime)s | %(levelname)-8s | %(name)s: %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"

    # Configure root logger
    logging.basicConfig(level=config.LOG_LEVEL, format=fmt, datefmt=datefmt)

    # Reduce SQL noise unless explicitly enabled
    logging.getLogger("sqlalchemy.engine").setLevel(config.SQL_LOG_LEVEL)

    # Forward Uvicorn’s loggers to the root logger
    for name in ("uvicorn", "uvicorn.error", "uvicorn.access"):
        logger = logging.getLogger(name)
        logger.handlers.clear()
        logger.propagate = True

    logging.getLogger(__name__).info(
        "Logging configured (env=%s, level=%s)", config.ENV, config.LOG_LEVEL
    )
