class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        totalSecsPoisoned = 0

        for i in range(len(timeSeries) - 1):
            if timeSeries[i] + duration < timeSeries[i + 1]:
                totalSecsPoisoned += duration
            else:
                totalSecsPoisoned += timeSeries[i + 1] - timeSeries[i]
        totalSecsPoisoned += duration

        return totalSecsPoisoned
