class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        area = 0
        max_area = 0
        for i in range(len(height) - 1):
            area = (r - l) * min(height[l], height[r])
            max_area = max(area, max_area)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return max_area


s = Solution()
print(s.maxArea([1, 2, 1]))
