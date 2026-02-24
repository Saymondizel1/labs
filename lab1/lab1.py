import unittest


def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2
    
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0 
        j = 0 
        k = 0 

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def sorted_squares(nums):
    s_nums = []
    for num in nums:
        s_nums.append(num ** 2)
    merge_sort(s_nums)
    
    return s_nums

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