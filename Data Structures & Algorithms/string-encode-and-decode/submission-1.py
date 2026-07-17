from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(w)}#{w}" for w in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        while s:
            i = s.find('#')
            length = int(s[:i])
            res.append(s[i + 1 : i + 1 + length])
            s = s[i + 1 + length :]
        return res
