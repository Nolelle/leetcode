# Time Complexitx:O(n)
# Space Complexitx: O(n);


class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercase_string = s.casefold()
        x = ""
        for letter in lowercase_string:
            if ord(letter) >= ord("a") and ord(letter) <= ord("z"):
                x += letter
        p1 = 0
        p2 = len(x) - 1
        if len(x) == 1:
            return True

        while p1 <= p2:
            if (x[p1] != x[p2]):
                return False
            p1 += 1
            p2 -= 1
        return True


s = Solution()
# print(s.isPalindrome("A man, a plan, a canal: Panama"))
# print(s.isPalindrome("race a car"))
# print(s.isPalindrome("0P"))
print(s.isPalindrome(" "))
# print(s.isPalindrome("AA"))
