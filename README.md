# labs
Repository for labs
Sorted Squares ArrayThis repository contains a Python implementation of an efficient algorithm to square a sorted array of integers and return a new sorted array.Problem DescriptionGiven an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.ExamplesExample 1:Input: nums = [-4, -2, 0, 1, 3]Output: [0, 1, 4, 9, 16]Explanation: After squaring, the array becomes [16, 4, 0, 1, 9]. After sorting, it becomes [0, 1, 4, 9, 16].Example 2:Input: nums = [1, 2, 3, 4, 5]Output: [1, 4, 9, 16, 25]Algorithmic Approach: Two PointersSince the input array is already sorted, the largest squares will come from either the very small negative numbers or the very large positive numbers. Using a Two Pointers approach allows us to solve this in $O(n)$ time complexity.Initialize two pointers: left at the start (0) and right at the end (n-1).Compare the absolute values of nums[left] and nums[right].Place the square of the larger value at the end of the resulting array and move the corresponding pointer inward.Repeat until the pointers meet.
How to Run
Ensure you have Python installed.
Clone the repository.
Run the script directly to execute the unit tests:
