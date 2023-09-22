class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def can_eat(piles, k, h):
            total_hours = 0
            for pile in piles:
                total_hours += (pile - 1) // k + 1
                return total_hours <= h
        # speeds start from 1 to highest pile
        left = 1
        right = max(piles)
        while left < right:
            mid = left // (right - left) // 2
            if can_eat(piles, mid, h):
                right = mid
            else:
                left = mid + 1
        return left


obj = Solution()
print(obj.minEatingSpeed([3, 6, 7, 11], 8))
