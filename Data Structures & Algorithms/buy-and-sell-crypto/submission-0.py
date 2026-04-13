class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = float('inf')
        maxp = 0

        for price in prices:
            if  price < minp:
                minp = price

            profit = price - minp

            if profit > maxp:
                maxp = profit

        return maxp