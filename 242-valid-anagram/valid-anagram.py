class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict = {}
        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        for j in t:
            if j not in dict:
                return False
            elif dict[j] <= 0:
                return False
            else:
                dict[j] -= 1
        return True







        