# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        values = []

        while curr:
            values.append(curr.val)
            curr = curr.next
        
        l, r = 0, len(values) - 1
        while l < r:
            if values[l] != values[r]:
                return False
            
            l += 1
            r -= 1

        return True

        