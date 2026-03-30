class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []

        #calculate interceptions by doing math.ceil((target - position) / speed)


        order_list = [(i, j) for i, j in zip(position, speed)]
        order_list = sorted(order_list)
        for i in range(len(order_list) - 1, -1, -1):
            speed = order_list[i][1]
            pos = order_list[i][0]
            intercept = (target - pos) / speed
            if stack and intercept <= stack[-1]:
                continue
            stack.append(intercept)
        return len(stack)


        

