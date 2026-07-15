class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_lowest = 100000000000
        profit = 0

        for i in range(len(prices)):
            if prices[i] < current_lowest:
                current_lowest = prices[i]
            elif prices[i] - current_lowest > profit:
                profit = prices[i] - current_lowest
        return profit
            

