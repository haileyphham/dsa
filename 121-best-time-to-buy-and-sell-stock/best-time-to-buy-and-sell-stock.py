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
            
            if profit > max_profit:
                max_profit = profit

            if prices[i] < curr_min:
                curr_min = prices[i]
        return max_profit

        if max_profit <= 0:
            return 0
            



        