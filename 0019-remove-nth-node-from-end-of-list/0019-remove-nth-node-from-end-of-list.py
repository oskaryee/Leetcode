# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        loc = (n + 1) * -1 # get the location of nth - 1
        
        # Lets get the length of the linked list
        node = head
        while node:
            loc += 1
            node = node.next

        # If we only have one node or we need to get rid of the head. 
        if loc < 0:
            return head.next

        # Lets get the location of the (nth - 1) node
        node = head
        for i in range(loc):
            node = node.next
        
        # Get rid of the nth node
        node.next = node.next.next

        return head
