class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        i, j = 0, 0
        common_letters = ""

        while i < len(str1) or j < len(str2):
            if i < len(str1) and str1[i] == str2[i]:
                common_letters += str1[i]

            if j < len(str2):
                common_letters += str2[j]

        return common_letters
