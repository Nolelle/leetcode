class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Input: nums = [0,1,0,3,12]
        # Output: [1,3,12,0,0]
        # have one pointer that tracks the latest non zero element in the array
        # another pointer that advances throught he array

        n = len(nums)
        nonzero = 0

        for i in range(n):
            if nums[i] != 0:
                nums[nonzero] = nums[i]
                nonzero += 1

        for j in range(nonzero, n):
            nums[j] = 0
