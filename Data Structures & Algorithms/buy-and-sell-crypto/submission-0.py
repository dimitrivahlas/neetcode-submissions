class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        count = 0

        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            count= max(count, price-lowest)
        return count
        