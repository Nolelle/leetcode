from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Base Case
        if root is None:
            return None
            
        if root.val == key:
            # Case #1 node has no children (leaf)
            if root.left is None and root.right is None:
                return None
            # Case #2 node has one children
            elif root.left is None or root.right is None:
                return root
            # Case #3 node has two children
            else:
                return self.findMinVal(root)

        # Recursive Case
        if root.val < key:
            return self.deleteNode(root.right, key)
        elif root.val > key:
            return self.deleteNode(root.left, key)

    def findMinVal(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #  Base case
        if root is None:
            return None;
        
        if root.left is None:
            return root
        
        # Recursive Case
        return self.findMinVal(root.left)
        


            

        


       