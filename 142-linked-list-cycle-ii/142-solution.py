# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Floyd's cycle detection algo (tortoise and hare algorithm)
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:   # instead of returning true when we find a cycle, we break out of the loop to find the entry point
                break
        else:                  # if no cycle found then we return null
            return None

        fast = head            # move fast back to beginning
        while fast != slow:    # move both pointers at the same speed until they inevitably meet at the entry point of the cycle
            slow = slow.next
            fast = fast.next
        
        return slow
        