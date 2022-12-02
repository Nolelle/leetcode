class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n != 0:
            n &= n - 1
            result += 1
        return result


s = Solution()
n = 0o00000000000000000000000000001011
print(s.hammingWeight(n))
