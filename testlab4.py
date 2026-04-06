import unittest
from lab4 import PriorityQueue

class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = PriorityQueue()

    def test_is_empty_initially(self):
        self.assertTrue(self.pq.is_empty())

    def test_insert_changes_empty_state(self):
        self.pq.insert("Тест", 1)
        self.assertFalse(self.pq.is_empty())

    def test_peek(self):
        self.pq.insert("A", 1)
        self.pq.insert("B", 10) 
        self.assertEqual(self.pq.peek(), ("B", 10))
        self.assertFalse(self.pq.is_empty())
        self.assertEqual(self.pq.extract_max(), ("B", 10))

    def test_priority_ordering(self):
        self.pq.insert("Низький", 1)
        self.pq.insert("Високий", 10)
        self.pq.insert("Середній", 5)
        self.assertEqual(self.pq.extract_max(), ("Високий", 10))
        self.assertEqual(self.pq.extract_max(), ("Середній", 5))
        self.assertEqual(self.pq.extract_max(), ("Низький", 1))
        self.assertTrue(self.pq.is_empty())

    def test_fifo_same_priority(self):
        self.pq.insert("Перший (пріоритет 5)", 5)
        self.pq.insert("Другий (пріоритет 5)", 5)
        self.pq.insert("Третій (пріоритет 5)", 5)
        self.assertEqual(self.pq.extract_max(), ("Перший (пріоритет 5)", 5))
        self.assertEqual(self.pq.extract_max(), ("Другий (пріоритет 5)", 5))
        self.assertEqual(self.pq.extract_max(), ("Третій (пріоритет 5)", 5))

    def test_mixed_inserts(self):
        self.pq.insert("A", 2)
        self.pq.insert("B", 5)
        self.pq.insert("C", 2)
        self.pq.insert("D", 10)
        self.assertEqual(self.pq.extract_max(), ("D", 10))
        self.assertEqual(self.pq.extract_max(), ("B", 5))
        self.assertEqual(self.pq.extract_max(), ("A", 2)) 
        self.assertEqual(self.pq.extract_max(), ("C", 2))

    def test_extract_from_empty_raises_error(self):
        with self.assertRaises(IndexError):
            self.pq.extract_max()

    def test_peek_from_empty_raises_error(self):
        with self.assertRaises(IndexError):
            self.pq.peek()

if __name__ == '__main__':
    unittest.main()