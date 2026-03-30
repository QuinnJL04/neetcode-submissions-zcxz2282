class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        result = l
        while l <= r:
            mid = (l+r) // 2
            time = 0
            for pile in piles:
                time_to_eat = math.ceil(pile / mid)
                time += time_to_eat
            if time > h:
                l = mid + 1
            else:
                result = mid
                r = mid - 1
        return result