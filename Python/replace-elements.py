class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        n = len(arr)
        right_max = arr[n - 1]
        if len(arr) == 1:
            return [-1]
        for i in range(n - 2, -1, -1):
            new_max = max(arr[i], right_max)
            arr[i] = right_max
            right_max = new_max
        arr[n - 1] = -1
        return arr


s = Solution()
print(s.replaceElements([17, 18, 5, 4, 6, 1]))
