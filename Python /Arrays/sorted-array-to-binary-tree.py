from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # empty array
        if not nums:
            return None
        
        # find the middle index
        mid = len(nums) // 2
        # array is sorted so make mid root
        root = TreeNode(nums[mid])




       