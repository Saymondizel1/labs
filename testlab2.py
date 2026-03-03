import unittest
class TestPokerSequence(unittest.TestCase):
    def test_example_1(self):
        cards = [0, 10, 15, 50, 0, 14, 9, 12, 40]
        
    def test_example_2(self):
        cards = [1, 1, 1, 2, 1, 1, 3]
        
    def test_example_3(self):
        cards = [5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 0, 0]
        
    def test_only_jokers(self):
        cards = [0, 0, 0]
        
    def test_no_jokers_no_sequence(self):
        cards = [10, 20, 30]
       

unittest.main()