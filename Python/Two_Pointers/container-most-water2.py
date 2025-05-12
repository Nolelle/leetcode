class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            current_length = right - left
            if height[left] <= height[right]:
                current_area = current_length * height[left]
                left += 1
            else:
                current_area = current_length * height[right]
                right -= 1
            if current_area > max_area:
                max_area = current_area

        return max_area


c = Solution()

print(c.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(c.maxArea([1, 1]))
