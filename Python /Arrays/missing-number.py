class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # given an input array of ints, i have to find the missing number
        # in the range of the given array.
        # Ill have to see all elements of the array first to confirm the missing number
        # so big o complexity is linear O(n)
        # Input: nums = [3,0,1]
        # Output: 2

        # optimal solution is sum formula or xor, my naive approach with more memory is
        # to store values in set to find the missing key.
        # Create an empty dict (or set).
        # Loop through the input array, adding each number as a key to the dict.
        # Loop from 0 to n (inclusive):
        # For each number j in this range, check if j is in the dict.
        # If not, j is the missing number.

        n = len(nums)

        if n == 0:
            return 0

        expected_sum = sum(nums)
        actual_sum = n * (n + 1) // 2

        return expected_sum - actual_sum
