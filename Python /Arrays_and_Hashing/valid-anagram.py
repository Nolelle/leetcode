class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict = {}

        for letter in s:
            dict[letter] = dict.get(letter, 0) + 1

        for letter in t:
            if letter not in dict or dict[letter] == 0:
                return False
            dict[letter] -= 1

        return True


obj = Solution()
# print(
#     obj.isAnagram(
#         "anagram",
#         "nagaram",
#     )
# )
print(
    obj.isAnagram(
        "aacc",
        "ccac",
    )
)
