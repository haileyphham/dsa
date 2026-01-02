class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = float(inf) #nothing is greater than this 1st price will be curr min
        max_profit = 0

        for price in prices:
            curr_min = min(curr_min, price) #want to find the smallest min as we iterate; keep it
            max_profit = max(max_profit, price-curr_min) #finding the max profit 
        return max_profit