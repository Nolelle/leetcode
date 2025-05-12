class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # we need to find a length of a subarray whose sum is greater than or equal to target we get the target other wise return 0
        left, right = 0, 1

        while right < len(nums):
            

            


c = Solution()

print(c.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(c.minSubArrayLen(4, [1, 4, 4]))
print(c.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
