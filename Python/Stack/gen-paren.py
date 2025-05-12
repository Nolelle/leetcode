class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # only add open paranthesis if open < n
        # only add close paranthesis if close < open
        # if open == close == n done
        stack = []
        res = []

        def backtrack(openN, closeN):
            # base case
            if openN == closeN == n:
                res.append("".join(stack))
                return
            # recursive case
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()

        backtrack(0, 0)
        return res


obj = Solution()
print(obj.generateParenthesis(3))
