# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        list = []

        if not root:
            return list
        
        if root.left:
            list = self.preorderTraversal(root.left)
            
        if root.right:
            list += self.preorderTraversal(root.right)
            
        return [root.val] + list
            
            