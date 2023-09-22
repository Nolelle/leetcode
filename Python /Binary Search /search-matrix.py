class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        m = len(matrix)
        n = len(matrix[0])
        row, col = 0, n - 1
        while row < m and col >= 0:
            current_element = matrix[row][col]

            if current_element == target:
                return True
            if current_element > target:
                col -= 1
            else:
                row += 1
        return False


obj = Solution()
# print(obj.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
print(obj.searchMatrix([[1], [3]], 3))
