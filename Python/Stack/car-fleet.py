class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Create a list of tuples containing position, speed pairs
        cars = sorted(zip(position, speed), reverse=True)

    # Calculate time taken for each car to reach the destination
        times = [(target - pos) / spd for pos, spd in cars]

    # Initialize the number of car fleets
        fleets = 0

    # Traverse the list and count the number of car fleets
        while times:
            slowest_car_time = times.pop(0)
            fleets += 1
            while times and times[0] <= slowest_car_time:
                times.pop(0)

        return fleets


obj = Solution()
print(obj.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
