class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest = 0
        numSet = set(nums)
        for n in nums:
            if n - 1 not in numSet:
                sequence = 0
                while n + sequence in numSet:
                    sequence += 1
            if sequence > longest:
                longest = sequence

        return longest


s = Solution()
print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
