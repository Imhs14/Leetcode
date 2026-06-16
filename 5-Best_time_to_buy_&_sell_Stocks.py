# LeetCode Problem 121: Best Time to Buy and Sell Stock
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy
# Category: Sliding Window
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0 
        for price in prices:
            profit  = price - min_price
            if price < min_price:
                min_price = price
            
            if profit > max_profit:
                max_profit = profit 
        return max_profit






