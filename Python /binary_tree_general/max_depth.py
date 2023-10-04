from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        left_depth = Solution().maxDepth(root.left)
        right_depth = Solution().maxDepth(root.right)
        return max(left_depth, right_depth) + 1


obj = Solution()
print(obj.maxDepth([3, 9, 20, None, None, 15, 7]))
