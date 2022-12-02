class Solution:
    def max_product(self, nums: list[int]) -> int:
        result = max(nums)
        current_min, current_max = 1, 1

        for i in nums:
            if i == 0:
                current_max, current_min = 1, 1
                continue
            temp = i * current_max

            current_max = max(i * current_max, i * current_min, i)
            current_min = min(temp, i * current_min, i)
            result = max(current_max, result)
        return result


s = Solution()
print(s.max_product([-3, -1, -1]))
