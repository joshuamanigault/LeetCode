class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        prefix = set()


        """
        Add all of the prefixes in arr1 to a set by 
        repeatedly negating the rightmost digit until the number becomes 0
        """
        for num in arr1:
            while num != 0 and num not in prefix:
                prefix.add(num)
                num = num // 10
        """
        Repeat the same process for arr2, but instead 
        after the while loop if the number is not equal to 0
        then update the longest variable with the maximum of the current longest
        and the length of the current prefix

        """
        longest = 0
        for num in arr2:
            while num != 0 and num not in prefix:
                num = num // 10
            
            if num != 0:
                longest = max(longest, len(str(num)))
        
        return longest