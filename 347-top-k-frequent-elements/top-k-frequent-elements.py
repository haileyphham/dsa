class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #loop through the array
        #if in dict, up the count
        #if not, add to dict and put count as 1
        #sort the list of the dictionary keys by its values
        # slice the list by k
        #return the list
        dict = {}

        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1

        sorted_items = sorted(dict.items(), key=lambda x: x[1], reverse=True)

        return [key for key, value in sorted_items[:k]]

        