class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string_split = s.split(' ')
        words = []
        for word in string_split:
            if len(word) > 0:
                words.append(word)
                
        return len(words[-1])
        
    
# Runtime 0 ms beats 100%, Memory 19.38 MB beats 10.98%