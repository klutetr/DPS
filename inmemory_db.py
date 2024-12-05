class TransactionError(Exception):
      
    pass

class InMemoryDB:
    def __init__(self):
        self._storage = {}
        self._transaction_storage = None
        self._transaction_in_progress = False

    def get(self, key: str) -> int:
        return self._storage.get(key)

    def put(self, key: str, val: int) -> None:
        if not self._transaction_in_progress:
            raise TransactionError("No transaction in progress")
        
        if self._transaction_storage is None:
            self._transaction_storage = dict(self._storage)
            
        self._transaction_storage[key] = val

    def begin_transaction(self) -> None:
        if self._transaction_in_progress:
            raise TransactionError("Transaction already in progress")
        
        self._transaction_in_progress = True
        self._transaction_storage = None

    def commit(self) -> None:
        if not self._transaction_in_progress:
            raise TransactionError("No transaction in progress")

        if self._transaction_storage:
            self._storage = self._transaction_storage.copy()
        
        self._transaction_storage = None
        self._transaction_in_progress = False

    def rollback(self) -> None:
        if not self._transaction_in_progress:
            raise TransactionError("No transaction in progress")
        
        self._transaction_storage = None
        self._transaction_in_progress = False
