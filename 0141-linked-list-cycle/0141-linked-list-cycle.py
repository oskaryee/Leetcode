# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head
        fast = head
        while fast and fast.next: # We only need to check the fast pointer...
            slow = slow.next
            fast = fast.next.next
            if slow == fast:      # We dont check the val. Only the reference
                return True
        
        return False

        # p1 = head
        
        # if head:
        #     p2 = head.next
        # else:
        #     return False

        # while p1 and p2:
        #     p1 = p1.next
        #     if p2.next:
        #         p2 = p2.next.next
        #     if p1 and p2 and p1 == p2:
        #         return True
        
        # return False
            
        
