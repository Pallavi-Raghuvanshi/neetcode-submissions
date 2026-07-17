class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1

        for j in t:
            if j not in d or d[j] == 0:
                return False
            d[j] -= 1
        
        return True
