class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = prices[0]
        profit = 0
        for i in prices:
            if i < price:
                price = i
            else:
                profit = max(profit, i-price)
        
        return profit