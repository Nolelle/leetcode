from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# use recrusive bfs to search both trees compareing each visited node return false if at any point false
# return true otherwise
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        # recursive case
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
