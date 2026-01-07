class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        output = []
        path = []

        def backtrack(i):
            if i == len(s):
                output.append(path.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    path.append(s[i:j+1])
                    backtrack(j + 1)
                    path.pop()

        backtrack(0)
        return output
        
        
