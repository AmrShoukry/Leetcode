class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = prices[0]
        max_sell = prices[0]

        for price in prices:
            if price < min_buy:
                min_buy = price
            if price - min_buy > max_profit:
                max_profit = price - min_buy
                max_sell = price
        return max_profit
