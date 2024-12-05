# DPS - In-Memory Database with Transaction Support

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

1. Add support for nested transactions to make the assignment more challenging and realistic.
2. Include concurrency requirements to test students' understanding of thread safety and synchronization.
3. Expand the value types beyond integers to include strings, lists, or JSON objects, making it more practical for real-world scenarios.
