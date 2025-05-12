class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        index1, index2 = 0, len(numbers) - 1

        while index1 < index2:
            current_sum = numbers[index1] + numbers[index2]
            if current_sum == target:
                return [index1 + 1, index2 + 1]
            elif current_sum < target:
                index1 += 1
            else:
                index2 -= 1


c = Solution()

print(c.twoSum([2, 7, 11, 15], 9))
