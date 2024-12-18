from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 = []
        leaf2 = []

        if root1 is None or root2 is None:
            return False
        
        self.traverseTree(root1,leaf1)
        self.traverseTree(root2, leaf2)
    
        return (leaf1 == leaf2)

        
    

        

    def traverseTree(self, root: Optional[TreeNode], array: list[int]) -> None:
        if root is None:
            return 
        
        if root.left is None and root.right is None:
            array.append(root.val)
            return
        
        self.traverseTree(root.left,array)
        self.traverseTree(root.right,array)
            



        

        