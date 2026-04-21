class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        l = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                k += 1
        
        return k