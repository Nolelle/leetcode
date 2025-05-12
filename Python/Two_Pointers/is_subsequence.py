class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        answer = ""

        while i < len(s):
            print("s: ", s[i])
            print("t: ", t[j])
            if s[i] == t[j]:
                i += 1
                j += 1
                answer += t[j]
                if answer == s:
                    return True
            else:
                j += 1

        return False


obj = Solution()
print(obj.isSubsequence("abc", "ahbgdc"))
