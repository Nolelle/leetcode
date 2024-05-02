class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            middle = (low + high) // 2
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                low = middle + 1
            else:
                high = middle - 1


obj = Solution()
print(obj.searchInsert([1, 3, 5, 6], 5))
