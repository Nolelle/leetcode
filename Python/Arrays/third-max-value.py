class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums_cleaned = list(set(nums))
        nums_cleaned.sort(reverse=True)
        n = len(nums_cleaned)

        if n >= 3:
            return nums_cleaned[2]
        else:
            return nums_cleaned[0]
