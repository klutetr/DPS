import unittest
from inmemory_db import InMemoryDB, TransactionError

class TestInMemoryDB(unittest.TestCase):
    def setUp(self):
        self.db = InMemoryDB()

    def test_get_nonexistent_key(self):
        """Test getting a key that doesn't exist returns None"""
        self.assertIsNone(self.db.get("A"))

    def test_put_without_transaction(self):
        """Test that put without a transaction raises an error"""
        with self.assertRaises(TransactionError):
            self.db.put("A", 5)

    def test_successful_transaction(self):
        """Test a successful transaction flow"""
        self.db.begin_transaction()
        self.db.put("A", 5)
        self.assertIsNone(self.db.get("A"))  # Should still be None until commit
        self.db.put("A", 6)
        self.db.commit()
        self.assertEqual(self.db.get("A"), 6)

    def test_commit_without_transaction(self):
        """Test that commit without a transaction raises an error"""
        with self.assertRaises(TransactionError):
            self.db.commit()

    def test_rollback_without_transaction(self):
        """Test that rollback without a transaction raises an error"""
        with self.assertRaises(TransactionError):
            self.db.rollback()

    def test_rollback(self):
        """Test rolling back changes"""
        self.assertIsNone(self.db.get("B"))
        self.db.begin_transaction()
        self.db.put("B", 10)
        self.db.rollback()
        self.assertIsNone(self.db.get("B"))

    def test_nested_transaction_error(self):
        """Test that starting a transaction while one is in progress raises an error"""
        self.db.begin_transaction()
        with self.assertRaises(TransactionError):
            self.db.begin_transaction()

if __name__ == '__main__':
    unittest.main()
