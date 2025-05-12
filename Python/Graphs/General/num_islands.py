class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        return 1


obj = Solution()
print(
    obj.numIslands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)
