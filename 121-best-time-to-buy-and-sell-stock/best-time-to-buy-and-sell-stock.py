class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ''' buy low(min)
            sell high (max)
            max profit max-min
            dict{price, index}

        '''
        curr_min = prices[0]
        max_profit = 0
     
        for i in range(len(prices)):
            profit = prices[i] - curr_min
            max_profit = max(max_profit, profit)
            curr_min = min(prices[i], curr_min)
        return max_profit

        #if max_profit <= 0:
            #return 0
            



        