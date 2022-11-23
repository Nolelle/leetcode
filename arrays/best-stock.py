class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1  # l = buy, r = sell
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)
            else:
                l = r
            r += 1
        return maxP


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
