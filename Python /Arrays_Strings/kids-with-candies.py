from tkinter.constants import W
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        results = []
        maxCandies = max(candies)

        for candy in candies:
            if candy + extraCandies >= maxCandies:
                results.append(True)
            else:
                results.append(False)

        return results
