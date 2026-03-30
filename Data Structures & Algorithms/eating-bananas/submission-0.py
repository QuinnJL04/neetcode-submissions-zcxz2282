class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #intuition is that we can only eat from one pile each hour therefore the max eating rate must be the max pile in piles
        #can use binary search to go from 1 - max_pile to find the minimum eating rate
        #while searching use the local eating rate and get the time it would take to eat from that pile (pile / eating rate) and add it to the time
        #if the time is too big shift the right pointer to the mid - 1 else shift the left pointer to the mid + 1
        r = max(piles)
        l = 1

        result = r

        while l <= r:
            mid = (l+r) // 2

            time = 0

            for p in piles:
                time += math.ceil(p / mid)
            
            if time <= h:
                result = mid 
                r = mid - 1
            else:
                l = mid + 1
        return result

