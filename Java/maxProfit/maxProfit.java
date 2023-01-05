//O(n2) solution
/*  class maxProfit {
    public int maxProfitFunction(int[] prices) {
        int maxProfit = 0;
        int profit = 0;
        for (int i = 0; i < prices.length - 1; i++) {
            for (int j = i + 1; j <= prices.length - 1; j++) {
                profit = prices[j] - prices[i];
                if (profit > maxProfit) {
                    maxProfit = profit;
                }
            }
        }
        return maxProfit;
    }
} */

// O(n) solution
class maxProfit {
    public int maxProfitFunction(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < minPrice) {
                minPrice = prices[i];
            } else if (prices[i] - minPrice > maxProfit) {
                maxProfit = prices[i] - minPrice;
            }
        }
        return maxProfit;
    }
}

class Solution {
    public static void main(String[] args) {
        maxProfit maxProfitObject = new maxProfit();
        int[] prices = { 1, 2 };
        System.out.println(maxProfitObject.maxProfitFunction(prices));
    }
}
