class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for price in prices:
            max_profit = max(price - min_price, max_profit)
            min_price = min(price, min_price)
        return max_profit

        
            

        #  price:      5   1   5   6   7   1
        #  min so far: 5   1   1   1   1   1
        #  profit:     2   6   6   6   6   6