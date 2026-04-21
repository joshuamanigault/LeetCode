import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
            
        return -1
    
# Runtime 83 ms beats 22.41%, Memory 19.63 MB beats 75.59%

class Solution2:
    def firstUniqChar(self, s: str) -> int:
        hset = collections.Counter(s)
        
        for i in range(len(s)):
            key = s[i]
            if hset[key] == 1:
                return i
        
        return -1

# Runtime 48 ms beats 81.36%, Memory 19.54 MB beats 93.96%