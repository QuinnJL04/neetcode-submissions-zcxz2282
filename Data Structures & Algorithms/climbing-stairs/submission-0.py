class Solution:
    def climbStairs(self, n: int) -> int:
        #input is n = number of steps
        #output is going to be the number of ways we can go up n steps going 1 or 2 steps at a time

        if n == 1:
            return 1
        if n == 2:
            return 2
        
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)