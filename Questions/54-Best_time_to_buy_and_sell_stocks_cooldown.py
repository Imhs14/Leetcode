# Question : 309. Best Time to Buy and Sell Stock with Cooldown
# Complexity : Time: O(N), Space: O(1)
# Topic/Category : Dynamic Programming / Greedy
# Difficulty : Medium
def maxProfit(prices: List[int]) -> int:
        maxx_profit = 0
        n = len(prices)
        if len(prices) <= 1: return 0
        i = 1
        while i < n:
            profit = prices[i] - prices[i-1]
            if profit > 0:
                maxx_profit += profit
                i += 2
            else:
                i += 1
        return maxx_profit

print(maxProfit([1,2,4])) # not done need to complete this one