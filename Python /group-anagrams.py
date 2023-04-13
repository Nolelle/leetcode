import collections


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()


# O(nlogn)
s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
