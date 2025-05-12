from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # base case
        if root is None:
            return False

        # recursive case
        targetSum -= root.val

        if root.left is None and root.right is None:
            return targetSum == 0

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(
            root.right, targetSum
        )
