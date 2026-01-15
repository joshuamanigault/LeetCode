class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            
            seen.add(num)
        
        return False

# Runtime: 12ms, beats 62.04%, Memory: 32.34MB, beats 23.09%