from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]):
        # base case
        if root is None:
            return 0
        # recursive case
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
