class Solution:
    def findMin(self, nums: list[int]) -> int:
        result = nums[0]
        l = 0
        r = len(nums) - 1
        m = int(len(nums) / 2)

        if nums[r] >= nums[l]:
            result = min(nums[l], result)
            return result

        if nums[m] >= nums[l]:
            for i in range(m, len(nums) - 1):
                result = min(nums[i], result)

        else:
            for i in range(0, m):
                result = min(nums[i], result)
        return result


s = Solution()
print(s.findMin([2, 1]))
