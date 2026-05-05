# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k: int):
        if not head:
            return None
        
        # grab all the linkedlist node values, store them in an array
        curr = head
        temp = []

        while curr:
            temp.append(curr.val)
            curr = curr.next
        
        # rotate the array with all the node values
        # [0, 1, 2] k = 4
        n = len(temp)
        if k > n:
            k = k % n
        rotated = temp[-k:] + temp[:-k]

        # construct a linkedlist with the rotated array
        head = ListNode()
        end = head

        for num in rotated:
            new_end = ListNode(num)
            end.next = new_end
            end = new_end
        
        return head.next
        