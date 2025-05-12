class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        t_pointer = 0

        while t_pointer < len(t) and s_pointer < len(s):
            if s[s_pointer] != t[t_pointer]:
                t_pointer += 1
            else:
                s_pointer += 1
                t_pointer += 1

        return s_pointer == len(s)


c = Solution()

print(c.isSubsequence("abc", "ahbgdc"))
print(c.isSubsequence("axc", "ahbgdc"))
print(c.isSubsequence("", "ahbgdc"))
