from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Since array is sorted ascending order, picking middle elements 
        # ensures we have the best chance of getting a height balanced bst 
        # WE need to utilize recursion and array indicies to build the tree

        # Recursion 
        # Base case: if the left index is greater than the right index, return None


        