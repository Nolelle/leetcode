class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        sum = 0

        for i in nums:
            if sum < 0:
                sum = 0
            sum += i
            max_sum = max(max_sum, sum)
        return max_sum


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
