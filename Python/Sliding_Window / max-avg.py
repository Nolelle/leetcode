from ast import Num
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        currentSum = sum(nums[0:k])
        maxAvgVal = currentSum / k
