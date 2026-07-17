class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            si = ''.join(sorted(i))
            if si not in d:
                d[si] = []
            d[si].append(i)
        return list(d.values())