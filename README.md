# lab2
Repository for labs
 Laboratory Work: Alternative Poker Variant (Merge Sort Implementation)
 Task Description

This laboratory work implements an algorithm to determine the longest possible sequence of consecutive cards in a modified poker variant.

Problem Statement

A player is dealt N cards (0 ≤ N ≤ 10000).

Each card has an integer value from 0 to 1,000,000.

0 represents a joker, which can be assigned any value.

The goal is to build the longest possible sequence of distinct consecutive numbers.

Wrap-around is not allowed.
 [999999, 1000000, 1, 2] is NOT a valid sequence.

 Objective

Implement the function:

def find_longest_sequence_merge(cards: list[int]) -> int:

The function returns the length of the longest consecutive sequence that can be formed using the given cards (including jokers).

 Algorithm Overview

This implementation consists of two main parts:

 Custom Merge Sort

Instead of using Python’s built-in sorting, the algorithm implements Merge Sort manually:

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)
def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result
 Longest Consecutive Sequence with Jokers

Steps:

Count jokers (0 values).

Remove duplicates using a set.

Sort unique cards using the custom merge_sort.

Apply the sliding window technique:

Calculate gaps between numbers.

Use jokers to fill gaps.

Track the maximum valid sequence length.

Ensure the result does not exceed the total number of cards.

 Full Solution
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def find_longest_sequence_merge(cards):
    jokers_count = 0
    unique_cards = []
    seen = set()
    
    for c in cards:
        if c == 0:
            jokers_count += 1
        elif c not in seen:
            unique_cards.append(c)
            seen.add(c)

    if not unique_cards:
        return jokers_count

    unique_cards = merge_sort(unique_cards)

    max_length = 0
    left = 0
    n_unique = len(unique_cards)
    
    for right in range(n_unique):
        gaps = (unique_cards[right] - unique_cards[left]) - (right - left)
        
        while gaps > jokers_count:
            left += 1
            gaps = (unique_cards[right] - unique_cards[left]) - (right - left)
            
        current_length = (right - left + 1) + jokers_count
        max_length = max(max_length, current_length)

    return min(max_length, len(cards))
⏱ Complexity Analysis

Merge Sort: O(n log n)

Sliding Window: O(n)

Overall Time Complexity: O(n log n)

Space Complexity: O(n)

 Examples
Example 1
cards = [0, 10, 15, 50, 0, 14, 9, 12, 40]

Output:

7
Example 2
cards = [1, 1, 1, 2, 1, 1, 3]

Output:

3
Example 3
cards = [5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 0, 0]

Output:

4
 Unit Testing

Testing is implemented using Python’s unittest module.

import unittest
from solution import find_longest_sequence_merge

class TestLongestSequence(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(
            find_longest_sequence_merge([0, 10, 15, 50, 0, 14, 9, 12, 40]),
            7
        )

    def test_example_2(self):
        self.assertEqual(
            find_longest_sequence_merge([1, 1, 1, 2, 1, 1, 3]),
            3
        )

    def test_example_3(self):
        self.assertEqual(
            find_longest_sequence_merge([5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 0, 0]),
            4
        )

if __name__ == "__main__":
    unittest.main()
 Running Tests
python -m unittest test_solution.py

or

python test_solution.py
 Project Structure
├── solution.py
├── test_solution.py
└── README.md
 Result

This laboratory work demonstrates:

Manual implementation of Merge Sort

Efficient handling of duplicates and jokers

Application of the sliding window technique

Unit testing using unittest
