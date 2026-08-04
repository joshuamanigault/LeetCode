class Solution:
    def occurrencesOfElement(self, nums: list[int], queries: list[int], x: int) -> list[int]:
        result = [-1] * len(queries)
        freq = {x: []}
        for i in range(len(nums)):
            if nums[i] != x:
                continue
            else:
                freq[x].append(i)
        
        if len(freq[x]) == 0:
            return result
        
        for i in range(len(queries)):
            query = queries[i]
            if query <= len(freq[x]):
                result[i] = freq[x][query-1]
            else:
                continue

        return result


        