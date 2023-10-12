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
        # recursive case

        return True


# obj = Solution()
# print(obj.isSameTree(([1, 2, 3]), ([1, 2, 3])))
