class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        l = []
        r = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] in l:
                    l = []
                    break
                l.append(s[j])
                r = max(r, len(l))
        return r