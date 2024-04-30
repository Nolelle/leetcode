class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            middle = (low + high) // 2
            print(f"Middle: {nums[middle]}")
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                low = middle + 1
                print(f"Low: {nums[low]}")
            else:
                high = middle - 1
                print(f"High {nums[high]}")


obj = Solution()

print(obj.searchInsert([1, 3, 5, 6], 5))
