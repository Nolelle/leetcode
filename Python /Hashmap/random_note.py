class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        for letter in magazine:
            if letter in dict.keys():
                dict[letter] += 1
            else:
                dict[letter] = 1

        for letter in ransomNote:
            if letter not in dict.keys() or dict[letter] == 0:
                return False
            dict[letter] -= 1
        return True


obj = Solution()
# print(obj.canConstruct("a", "b"))
# print(obj.canConstruct("aa", "ab"))
# print(obj.canConstruct("aa", "aab"))
print(obj.canConstruct("aab", "baa"))
