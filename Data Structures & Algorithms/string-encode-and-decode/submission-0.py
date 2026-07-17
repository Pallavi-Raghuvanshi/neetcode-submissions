from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        e = ''
        for word in strs:
            e += str(len(word)) + '#' + word
        return e

    def pop(self, s: str, i: int):
        l = list(s)
        a = l.pop(i)
        return a, ''.join(l)

    def decode(self, s: str) -> List[str]:
        result = []
        
        # Keep processing until the encoded string is completely empty
        while s:
            # 1. Read the length of the upcoming word
            length_str = ''
            while True:
                c, s = self.pop(s, 0)
                if c == '#':  # Stop reading the length when we hit the delimiter
                    break
                length_str += c
            
            word_length = int(length_str)
            
            # 2. Pop the exact number of characters belonging to the word
            word = ''
            for _ in range(word_length):
                char, s = self.pop(s, 0)
                word += char
                
            result.append(word)
            
        return result
