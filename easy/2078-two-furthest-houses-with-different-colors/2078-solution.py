# https://leetcode.com/problems/two-furthest-houses-with-different-colors/description/?envType=daily-question&envId=2026-04-20
# difficulty: easy
# tags: Greedy, Array

class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        left_most = colors[0]
        right_most = colors[-1]
        n = len(colors)
        max_distance = 0

        # Start from left most -> Backtrack from rightside
        for i in range(n - 1, -1, -1):
            if colors[i] != left_most:
                max_distance = max(max_distance, i)
                break

        # Start from right most -> Move ahead from left side
        for i in range(0, n - 1):
            if colors[i] != right_most:
                max_distance = max(max_distance, (n - 1) - i)
                break 
        
        return max_distance
            
        