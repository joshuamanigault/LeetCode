class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        
        total = 0
        current = 0

        for actual, minimum in tasks:
            if current < minimum:
                total += minimum - current
                current = minimum
            current -= actual
        
        return total