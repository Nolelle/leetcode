class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        # nums sorted int array, range [a,b] inclusive integer range
        # return smallest sorted list of ranges that
        # cover all the numbers in the array exactly.
        # nums = [0,1,2,4,5,7]
        # ["0->2","4->5","7"]
        # Explanation: The ranges are:
        # [0,2] --> "0->2"
        # [4,5] --> "4->5"
        # [7,7] --> "7"

        ans = []
        # edgecase of empty input
        if len(nums) == 0:
            return ans

        start = 0
        for i, num in enumerate(nums):

            # we found end of range
            if len(nums) - 1 == i or nums[i] + 1 != nums[i + 1]:
                if i == start:
                    ans.append(f"{nums[start]}")
                else:
                    ans.append(f"{nums[start]}->{nums[i]}")
                start = i + 1

        return ans
