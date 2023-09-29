class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        reversed_nums = list(reversed(nums))

        print(reversed_nums)


obj = Solution()
print(obj.rotate([1, 2, 3, 4, 5, 6, 7], 3))
