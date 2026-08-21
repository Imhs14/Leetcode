# Question : 121. Best Time to Buy and Sell Stock
# Complexity : Time: O(N), Space: O(1)
# Topic/Category : Sliding Window
# Difficulty : Easy
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
'''prices =
[7, 1, 5, 3, 6, 4]
Output
5
'''

"""
prices = [7,1,5,3,6,4]
o/p = 5
"""
