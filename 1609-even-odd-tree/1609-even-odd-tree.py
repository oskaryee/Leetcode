# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return 0
        
        queue = [root]
        level = 0

        while queue:
            prev = float('inf') if level % 2 else 0

            for i in range(len(queue)): # I not used, only need the for loop
                node = queue.pop(0)
                # print(str(i) + " Node: " + str(node.val), end=", ")

                if (level % 2 and (node.val % 2 or node.val >= prev)):
                    return False

                if ((not level % 2) and ((not node.val % 2 )or node.val <= prev)):
                    return False

                prev = node.val
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            level += 1
            # print()
        return True
        