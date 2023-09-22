class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashmap = set()
        for num in nums:
            if num in hashmap:
                return True
            hashmap.add(num)
        return False


obj = Solution()
print(obj.containsDuplicate([1, 2, 3, 1]))
