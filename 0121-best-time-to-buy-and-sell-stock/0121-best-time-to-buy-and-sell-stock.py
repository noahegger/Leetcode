# Brute force nested for loop is bad
# Can we go through the prices only once?
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                if price - min_price > max_profit:
                    max_profit = price - min_price
                # max_profit = max(max_profit, price-min_price)
        return max_profit

        
        