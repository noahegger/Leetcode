# Brute force nested for loop is bad
# Can we go through the prices only once?
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]

        for price in prices[1:]:
            if price < min_price:
                min_price = price
            profit = max(profit, price-min_price)
        return profit

        
        