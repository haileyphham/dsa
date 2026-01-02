class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #index through the nums array
        #remainder = target - nums[i] 
        #if remainder in seen, return [seen[remainder],nums]
        #if not add to seen and move on

        seen = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in seen:
                return [seen[remainder], i]
            else: 
                seen[nums[i]] = i


        
        