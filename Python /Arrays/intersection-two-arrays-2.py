class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        ans = []
        dict = {}
        # dict = {num: int, countofOccurences: int}

        if n1 > n2:
            nums1, nums2 = nums2, nums1

        for num in nums1:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        for num in nums2:
            if num in dict:
                if dict[num] > 0:
                    ans.append(num)
                    dict[num] -= 1

        return ans
