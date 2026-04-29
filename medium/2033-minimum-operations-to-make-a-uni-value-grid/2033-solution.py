class Solution:
    def minOperations(self, grid: List[List[int]], x:int) -> int:
        flat = sorted([item for sublist in grid for item in sublist])
        median = flat[len(flat) // 2]
        operations = 0

        for num in flat:
            if (num % x) != (median % x):
                return -1
        
        for num in flat:
            operations += abs(median - num) // x
        
        return operations
