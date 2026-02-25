class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        window = nums[:k]
        current_sum = sum(window)

        freq = {}
        for num in window:
            freq[num] = freq.get(num, 0) + 1
        

        max_sum = current_sum if len(freq) == k else 0


        for i in range(n - k):
            left_val = window.pop(0)
            current_sum -= left_val
            freq[left_val] -= 1
            if freq[left_val] == 0:
                del freq[left_val]
            

            new_val = nums[i + k]
            window.append(new_val)
            current_sum += new_val
            freq[new_val] = freq.get(new_val, 0) + 1

            if len(freq) == k:
                max_sum = max(max_sum, current_sum)
        
        return max_sum
        