class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A
        total = len(A) + len(B)
        left = 0
        right = len(A)
