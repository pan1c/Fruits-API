# Fruit API

A tiny FastAPI micro‑service that lets you store and retrieve fruits in a PostgreSQL database.

It was built for the technical exercise *"Develop a simple Fruits API"*.

---

## Quick start (local)

```bash
# 1 — Clone the repo
$ git clone <your‑fork‑url> && cd Fruits-API

# 2 — Create environment file with DB credentials (or accept defaults)
$ cp .env.example .env
```

### Running locally

```bash
$ docker compose up --build
```

### Running tests

```bash
$ docker compose --profile test up --build --abort-on-container-exit test
```

* The API will be reachable at **[http://localhost:8000](http://localhost:8000)**.
* Interactive documentation lives at **[http://localhost:8000/docs](http://localhost:8000/docs)** (Swagger UI).

---

## API reference (v1)

| Method | Path                  | Description                              |
| ------ | --------------------- | ---------------------------------------- |
| `GET`  | `/api/v1/fruits`      | List **all** fruits                      |
| `GET`  | `/api/v1/fruits/{id}` | Get a **single** fruit by its numeric ID |
| `POST` | `/api/v1/fruits`      | Create a new fruit (JSON payload)        |

### 1 — List fruits

```bash
curl http://localhost:8000/api/v1/fruits
```

```json
[
  {"id": 1, "fruit": "apple",  "color": "red"},
  {"id": 2, "fruit": "banana", "color": "yellow"}
]
```

### 2 — Get a specific fruit

```bash
curl http://localhost:8000/api/v1/fruits/1
```

```json
{"id": 1, "fruit": "apple", "color": "red"}
```

If the fruit doesn't exist the API returns `404 Not Found`.

### 3 — Add a fruit

```bash
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"fruit": "orange", "color": "orange"}' \
     http://localhost:8000/api/v1/fruits
```

```json
{"id": 3, "fruit": "orange", "color": "orange"}
```

The new fruit is persisted in PostgreSQL; subsequent calls to `/fruits` will include it.

---
