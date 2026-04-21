class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
        
    
# Runtime 0 ms beats 100%, Memory 19.38 MB beats 10.98%