class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2  # this avoids overflow
            guess = nums[middle]
            if target == guess:
                return middle
            if guess > target:
                right = middle - 1
            else:
                left = middle + 1
        return -1


obj = Solution()
print(obj.search([-1, 0, 3, 5, 9, 12], 9))
