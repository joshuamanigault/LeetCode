class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}
        freq2 ={}

        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1
            freq2[t[i]] = freq2.get(t[i], 0) + 1

        return freq == freq2
        
    # Runtime 11ms beats 74.92%, Memory 19.44MB beats 19.20%