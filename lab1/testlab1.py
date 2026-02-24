import unittest
from lab1 import sorted_squares,merge_sort
class Test(unittest.TestCase):
    def test_1(self):
        nums = [-4, -2, 0, 1, 3]
        expected = [0, 1, 4, 9, 16]
        self.assertEqual(sorted_squares(nums), expected)
        print("test_1 пройдено!")

    def test_2(self):
        nums = [1, 2, 3, 4, 5]
        expected = [1, 4, 9, 16, 25]
        self.assertEqual(sorted_squares(nums), expected)
        print("test_2 пройдено!")

    unittest.main()