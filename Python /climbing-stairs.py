class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        one, two = 1, 2
        for i in range(3, n + 1):
            three = one + two
            one = two
            two = three
        return two


s = Solution()
print(s.climbStairs((3)))
