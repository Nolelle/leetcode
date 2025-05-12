class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # we need to find two indicies if there values are equal and the difference is less then or equal to k
        # Input: nums = [1,2,3,1], k = 3  Output: true indicies 0 and 3 are equal with a value of one, abs|0-3| <= 0
        # k(nums[i]): (array values) v(i): (array index)
        dict = {}

        for i, num in enumerate(nums):
            if num in dict and abs(i - dict[num]) <= k:
                return True

            dict[num] = i

        return False
