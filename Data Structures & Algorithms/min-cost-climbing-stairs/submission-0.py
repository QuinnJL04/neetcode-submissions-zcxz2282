class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #dp[i] = min cost to reach step at i
        # [10, 15, 20] append 0 to index 3
        
        cost.append(0)

        for i in range(len(cost) - 3, -1 ,-1):
            #store the min cost between making 1 jump or 2 jumps
            cost[i] = cost[i] + min(cost[i + 1], cost[ i + 2])
        
        return min(cost[0], cost[1])
