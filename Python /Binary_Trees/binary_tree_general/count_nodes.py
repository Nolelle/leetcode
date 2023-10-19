from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find_height(self, root: Optional[TreeNode], height):
        if root is None:
            return height
        height += 1
        self.find_height(root.left, height)

    def countNodes(self, root: Optional[TreeNode]) -> int:
        # first find the height of the tree this takes O(n)
        # we can do this by traversing the left most nodes till we find None
        count = 0
        height = 0
        height += self.find_height(root.left, height)
        count += 2**height - 1

        # then using the height, we can use that info decide whether or not we count
