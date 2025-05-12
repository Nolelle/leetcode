from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
        if root is None:
            return None
        # recursive case
        root.left, root.right = root.right, root.left
        self.invert_tree(root.right)
        self.invert_tree(root.left)
        return root
