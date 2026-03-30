class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #define a range of eating rates
        #binary search and test each rate out until you find the minimum rate

        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l+r)//2
            t = 0
            for pile in piles:
                t += math.ceil(float(pile) / k)
            if t <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        
        return res

            




                                
                