class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #fleets are counted as the cars that reach a position at different times
        #if a car reaches the car ahed of it at its dest its a part of the same fleet

        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []

        for p, s in pairs:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
