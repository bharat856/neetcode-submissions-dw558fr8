class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(key = lambda x: x[0], reverse = True)
        stack = []
        for position, speed in cars:
            time = (target - position) / speed
            if  time in stack:
                continue
            else:
                stack.append(time)
        return len(stack)