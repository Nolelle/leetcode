class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_string = ("".join([char for char in s if char.isalnum()])).lower()
        left, right = 0, (len(formatted_string) - 1)

        while left <= right:
            if formatted_string[left] != formatted_string[right]:
                return False
            left += 1
            right -= 1
        return True


s = Solution()

# print(s.isPalindrome("A man, a plan, a canal: Panama"))
# print(s.isPalindrome("race a car"))
print(s.isPalindrome(" "))
# print(s.isPalindrome("0P"))
