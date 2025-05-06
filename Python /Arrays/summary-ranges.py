class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        # nums sorted int array, range [a,b] inclusive integer range
        # return smallest sorted list of ranges that
        # cover all the numbers in the array exactly.
        ans = []
        start = 0

        for i, num in enumerate(nums):
            if nums[i] + 1 != nums[i + 1]:
                start = i
