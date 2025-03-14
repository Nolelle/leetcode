class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        # run through flowerbed array.
        # check to see if it is a one or zero
        # if it is a one it is not empty
        # we then need to check the adjacent slots to see if it is empty
        # if it is then we increment a can plant counter
        # if adjacent slots are not empty we move to the next slot
        # repeat until we reach the end of the array
        # if the can plant counter is greater than or equal to n we return true
        # otherwise we return false
        can_plant = 0
        for i in range(len(flowerbed)):
            # first element
            if i == 0:
                if flowerbed[i + 1] == 0:
                        can_plant += 1
            # second element
            elif i == len(flowerbed) - 1:
                if flowerbed[i - 1] == 0:
                    can_plant += 1
            # all other elements
            else:
                if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    can_plant += 1

        return can_plant >= n
