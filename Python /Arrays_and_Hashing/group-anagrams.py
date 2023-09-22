class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dict = {}
        for word in strs:
            for letter in word:
                dict[letter] = dict.get(letter, 0) + 1


obj = Solution()
print(obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
