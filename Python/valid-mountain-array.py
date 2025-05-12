class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        i = 0
        n = len(arr)
        if n < 3:
            return False

        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        if i == 0 or i == n - 1:
            return False

        while i + 1 < n and arr[i] > arr[i+1]:
            i += 1

        return i == n - 1


s = Solution()
print(s.validMountainArray([0, 1, 2, 4, 2, 1]))
