class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        ans = set()

        if n1 > n2:
            nums1, nums2 = nums2, nums1
        nums1_set = set(nums1)

        for num in nums2:
            if num in nums1_set:
                ans.add(num)

        return list(ans)
