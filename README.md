# DPS - In-Memory Database

This project implements an in-memory key-value database that supports atomic transactions. The database allows for operations like get, put, commit, and rollback within transaction boundaries.

## Requirements
- Python 3.6 or higher

## How to Run

1. Clone this repository
2. Navigate to the project directory
3. Run the tests:
```bash
python -m unittest test_inmemory_db.py
```

## Usage Example
```python
from inmemory_db import InMemoryDB

db = InMemoryDB()
db.begin_transaction()  # Start a transaction
db.put("A", 5)         # Set A to 5
db.commit()            # Commit changes
value = db.get("A")    # Get value of A (returns 5)
```

## Future Assignment Improvements

Add a required testing file to the project so students can practice writing unit tests.
