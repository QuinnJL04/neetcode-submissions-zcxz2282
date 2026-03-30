class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        min_rate = 1
        max_rate = max(piles)
        result = 1
        while min_rate <= max_rate:
            mid = (min_rate + max_rate) // 2
            time_to_eat = 0
            for pile in piles:
                time_to_eat += math.ceil(pile / mid)
            if time_to_eat > h:
                min_rate = mid + 1
            else:
                max_rate = mid - 1
                result = mid

        return result