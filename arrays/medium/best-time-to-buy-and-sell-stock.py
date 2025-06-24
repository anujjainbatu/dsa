# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_price = float("inf")
        max_profit = 0
        
        for curr_price in prices:
            if curr_price > min_price:
                curr_profit = curr_price - min_price
                max_profit = max(curr_profit, max_profit)
            if curr_price < min_price:
                min_price = curr_price
            
            
        return max_profit
