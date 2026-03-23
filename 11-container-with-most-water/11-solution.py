class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_area
        
        # Runtime 43 ms (Beats 95.65%) | Memory 29.54 MB (Beats 55.61%)