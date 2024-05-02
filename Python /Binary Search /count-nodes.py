from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)

        if left_depth == right_depth:
            return (2**left_depth) + self.countNodes(root.right)
        else:
            return self.countNodes(root.left) + (2**right_depth)

    def get_depth(self, node: Optional[TreeNode]):
        depth = 0
        while node:
            node = node.left
            depth += 1

        return depth

    def countNodes2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + self.countNodes2(root.left) + self.countNodes2(root.right)
