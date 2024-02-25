# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        q = l2
        carry = 0
        result_head = ListNode(-1)
        i_node = result_head
        
        while p or q:  # values are not None
            x = p.val if p else 0
            y = q.val if q else 0
            out = x + y + carry
            carry = out // 10
            i_node.next = ListNode(out % 10)
            i_node = i_node.next
            p = p.next if p else None
            q = q.next if q else None
        
        if carry > 0:
            i_node.next = ListNode(carry)
        
        return result_head.next