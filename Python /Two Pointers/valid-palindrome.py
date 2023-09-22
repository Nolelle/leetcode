class Solution:
    def isPalindrome(self, s: str) -> bool:
        parsed_string = ""
        for letter in s:
            if letter.isalnum():
                parsed_string += letter.lower()
        i = 0
        j = len(parsed_string) - 1

        while i < j:
            if parsed_string[i] != parsed_string[j]:
                return False
            i += 1
            j -= 1
        return True


obj = Solution()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))

#     parsed_string = ''.join(c.lower() for c in s if c.isalnum())

#    return parsed_string == parsed_string[::-1]
