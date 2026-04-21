import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        heap = [(-freq, number) for number, freq in freq.items()]
        heapq.heapify(heap)

        result = []

        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result
    

# Runtime: 7 ms, beats 54.15%, Memory: 23.13 MB, beats 20.41%