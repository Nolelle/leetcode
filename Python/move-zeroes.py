class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        size = len(nums)
        i = 0
        j = 0
        while (j < size - 1) and (i < size - 1):
            if nums[i] == 0:
                if nums[j + 1] != 0:
                    temp = nums[i]
                    nums[i] = nums[j + 1]
                    nums[j + 1] = temp
            else:
                i += 1
                j += 1
        return nums


s = Solution()
# print(s.moveZeroes([0, 1, 0, 3, 12]))
# print(s.moveZeroes([2, 1]))
print(s.moveZeroes([4, 2, 4, 0, 0, 3, 0, 5, 1, 0]))
