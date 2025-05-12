class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in dict:
                return [dict[complement], i]
            dict[num] = i


obj = Solution()
print(obj.twoSum([2, 7, 11, 15], 9))
