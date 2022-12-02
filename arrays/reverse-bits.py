class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
        for i in range(32):
            output <<= 1
            if n & 1:
                output += 1
            n >>= 1
        return output


s = Solution()
print(s.reverseBits(0n00000010100101000001111010011100))
