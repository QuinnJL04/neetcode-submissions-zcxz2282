class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        result = r
        while l <= r:
            mid = (l + r) // 2
            print(mid)
            time_to_eat = 0
            for pile in piles:
                time_to_eat += math.ceil(pile/mid)
            if time_to_eat <= h:
                result = mid
                r = mid - 1
            else:
                l = mid + 1
        return result