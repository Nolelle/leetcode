class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        s_dict = {}
        t_dict = {}

        for i in range(n):
            if s[i] not in s_dict:
                s_dict[s[i]] = t[i]

        for j in range(n):
            if t[j] not in t_dict:
                t_dict[t[j]] = s[j]
        print(s_dict)
        print(t_dict)

        for k in range(n):
            if s_dict[s[k]] != t[k]:
                return False

        return True


obj = Solution()
# print(obj.isIsomorphic("egg", "add"))
# print(obj.isIsomorphic("foo", "bar"))
print(obj.isIsomorphic("badc", "baba"))
# print(obj.isIsomorphic("abab", "baba"))
