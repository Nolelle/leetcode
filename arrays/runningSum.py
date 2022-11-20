class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        answer = []
        answer.append(nums[0])
        previous_answer = nums[0]
        for x in range(1, len(nums)):
            answer.append(previous_answer + nums[x])
            previous_answer = answer[x]
        return answer


s = Solution()
print(s.runningSum([1, 2, 3, 4]))
