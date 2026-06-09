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






'''for i in prices:
            if i == min(prices):
                buy = min(prices)
        
        for i in prices #[buy:]:
            if i == max(prices[buy:]):
                print(sell = i )
            else:
                print(sell = 0 )
        return '''