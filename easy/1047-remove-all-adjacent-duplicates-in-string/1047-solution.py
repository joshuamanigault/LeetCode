# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
# difficulty: easy
# tags: String, Stack

class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        Example 1 - Walkthrough

        abbaca

        [a] 
        [a, b]
        [a] -> Ran into second B
        [] -> Ran into second A
        [c]
        [c, a]

        # Example 2 - walkthrough 
        
        azxxzy

        [a]
        [a, z]
        [a, z, x]
        [a, z] -> Ran into second X, pop the top item
        [a] -> Ran into second Z, pop the top item
        [a, y] -> Final string
        """
    
        stack = []
        for char in s:
            if len(stack) < 1:
                stack.append(char)
            else:
                top_item = stack[-1]
                if top_item == char:
                    stack.pop()
                else:
                    stack.append(char)

        return "".join(stack)