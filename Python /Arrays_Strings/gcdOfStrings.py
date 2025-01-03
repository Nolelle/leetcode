class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
       # theres no gcd if concatenation of str1 and str2
       # is not equal to concatenation of str2 and str1
        if str1 + str2 != str2 + str1:
            return ""
        gcd_length = self.gcd(len(str1), len(str2))
        return str1[:gcd_length]

    def gcd(self,a:int, b:int) -> int:
        while b:
            a, b = b, a % b
        return a
