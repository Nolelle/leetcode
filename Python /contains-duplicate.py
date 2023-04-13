# Time Complexity: O(nlogn)
# Space Complexity: O(1)
# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         a = sorted(nums)
#         i = 0
#         while i < len(nums) - 2:
#             if (a[i] == a[i+1]):
#                 return True
#             i += 1
#         return False

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashmap = set()
        for i in nums:
            if i in hashmap:
                return True
            hashmap.add(i)
        return False


s = Solution()
print(s.containsDuplicate([0, 4, 5, 0, 3, 6]
                          ))
