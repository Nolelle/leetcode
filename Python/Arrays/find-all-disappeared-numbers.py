class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        nums_set = set(nums)
        ans = []

        for i in range(1, n + 1):
            if i not in nums_set:
                ans.append(i)

        return ans
