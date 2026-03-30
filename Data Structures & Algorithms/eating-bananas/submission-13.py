class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #define a range of eating rates
        #binary search and test each rate out until you find the minimum rate

        l, r = 1, max(piles)
        res = 0
        while l <= r:
            k = (l+r)//2
            time = 0
            for pile in piles:
                time += math.ceil(pile / k)
            
            if time > h:
                l = k + 1
            elif time <= h:
                res = k
                r = k - 1
        
        return res


            

            




                                
                