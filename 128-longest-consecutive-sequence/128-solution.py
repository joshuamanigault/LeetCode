class Solution:
    def longestConsecutive(self, nums: list) -> int:
        numbers = set(nums)
        longest = 0

        for num in nums:
            length = 1
            if num -1 not in numbers:
                while num + 1 in numbers:
                    num += 1
                    length += 1
            
            longest = max(longest, length)
        
        return longest
        