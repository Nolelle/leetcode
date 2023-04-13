class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        stack = []
        result = [0] * n
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                result[j] = i - j
            stack.append(i)
        return result


obj = Solution()
print(obj.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
