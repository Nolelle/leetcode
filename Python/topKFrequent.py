import collections


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dict = collections.Counter(nums)
        most_common = dict.most_common(k)
        print(most_common)
        # ans = []
        # # ans.clear()
        # for i in most_common:
        #     ans.append(i[0])
        return most_common


s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
