class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_count = 0
        seen = {} #where key=char, val=index


        for r in range(len(s)):
            if s[r] in seen:
                l = max(l,seen[s[r]] + 1)
                
            
            #if s[r] not in seen,
            seen[s[r]] = r
            max_count = max(max_count, r-l+1)
        return max_count
            
        
            
        

        