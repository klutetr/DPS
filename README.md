# DPS - In-Memory Database

This project implements an in-memory key-value database that supports atomic transactions. The database allows for operations like get, put, commit, and rollback within transaction boundaries.

## Requirements
- Python 3.6 or higher

## How to Run

1. Clone this repository
2. Navigate to the project directory
3. Run all tests:
```bash
python -m unittest test_inmemory_db.py -v
```

To run a specific test:
```bash
python -m unittest test_inmemory_db.TestInMemoryDB.test_rollback -v
```

## Unit Tests
The test suite includes verification of:
- Basic operations (get/put)
- Transaction isolation
- Error handling
- Transaction rollback
- Edge cases (nested transactions, operations without transactions)

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

1. **Testing Requirements**:
   - Provide a skeleton test file with empty test cases for students to implement
   - Add requirements for minimum test coverage percentage
   - Require students to write edge case tests

2. **New Features**:
   - Add support for different value types (strings, lists)
   - Implement a size limit for the database
   - Add a method to list all keys in the database
   - Add support for deleting keys

3. **Documentation**:
   - Require API documentation in a specific format
   - Add requirements for error message documentation
   - Require a design document explaining implementation choices
