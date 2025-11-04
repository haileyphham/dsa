class Solution:
    def rob(self, nums: List[int]) -> int:
        #adjectent 
        if not nums:
            return 0

        prev = 0
        prev2 = 0

        for money in nums:
            rob_curr = money + prev2
            skip_curr = prev
            curr_best = max(rob_curr, skip_curr)
            
            prev2 = prev
            prev = curr_best
            

        return prev
        