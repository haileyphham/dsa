class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_count = 0

        for num in seen:
            if num-1 not in seen: #if prev num not in set, 
                current = num
                count = 1 #only 1 elem is in sequence rn

                while current+1 in seen: #count if next num in set
                    current += 1
                    count += 1
                max_count = max(max_count, count)
        return max_count




