class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = float(inf)
        max_profit = 0

        for i in range(len(prices)):
            curr_min = min(prices[i], curr_min)
            max_profit = max(max_profit, prices[i] - curr_min)
        return max_profit

