class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
            print(missing)
        return missing


s = Solution()
print(s.missingNumber(([3, 0, 1])))
