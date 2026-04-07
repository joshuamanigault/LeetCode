class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]

        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
        
        return prefix
        
        # Runtime 0 ms beats 100%, Memory 19.24 MB beats 81%