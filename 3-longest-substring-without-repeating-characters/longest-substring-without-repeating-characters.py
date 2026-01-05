class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = {} #key: char, value: index
        curr_max = 0

        for right in range(len(s)):
            if s[right] in seen and seen[s[right]] >= left: #invalid bc its in the window rn
                left = seen[s[right]] + 1
            seen[s[right]] = right
            curr_max = max(curr_max, right-left + 1)
        return curr_max
                



        