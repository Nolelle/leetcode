class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = [1] * len(nums)  # fills answer array with ones
        prefix = 1 # prefix outside of array is assumed to be one
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        postfix = 1 # postfix outside of array is assumed to be one 
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        return answer


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
