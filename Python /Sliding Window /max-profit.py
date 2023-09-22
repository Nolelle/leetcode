class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        i = 0
        j = len(prices) - 1
        while i < j:
            if prices[i] - prices[j] < 0:
                j -= 1


obj = Solution()
print(obj.maxProfit([7, 1, 5, 3, 6, 4]))
