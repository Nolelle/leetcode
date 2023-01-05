# Time Complexity: O(nlogn)
# Space Complexity: O(logn)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        x = sorted(s)
        y = sorted(t)

        if x != y:
            return False

        return True


s = Solution()
print(s.isAnagram("anagram", "nagaram"))
