# Fruits API

REST API built with FastAPI, chosen for its:
- Automatic OpenAPI documentation
- Built-in request validation
- Modern async support
- High performance

## Project Structure

```
app/
├── modules/          # Feature modules
│   └── fruit/       # Fruit-related endpoints
│       ├── router.py    # API routes
│       ├── models.py    # Database models
│       ├── schemas.py   # Pydantic schemas
│       └── crud.py      # Database operations
├── main.py          # Application entry point
├── config.py        # Configuration & env vars
├── db.py            # Database connection
└── logger.py        # Logging setup
```
