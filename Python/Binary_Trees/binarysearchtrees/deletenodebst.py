from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # Find the node to delete
        if key < root.val:
            root.left = self.deleteNode(root.left,key)
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)
        else:
            # Node found
            # Case 1: no children 
            if not root.left and not root.right:
                return None
            # Case 2: One child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # Case 3: Two children
            min_node = self.findMin(root.right)
            if min_node:
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)
        return root

    def findMin(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node:
            return None
        
        current = node
        while current.left:
            current = current.left
        return current






       