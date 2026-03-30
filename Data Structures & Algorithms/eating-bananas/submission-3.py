class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #search through the eating rates using binary search

        #create a range from the max eating rate to the min eating rate

        max_rate = max(piles)
        min_rate = 1
        result = max_rate
        while min_rate <= max_rate:
            mid = (min_rate + max_rate) // 2
            time_to_eat = 0
            for pile in piles:
                time_to_eat += math.ceil(pile / mid)
            if time_to_eat > h:
                min_rate = mid + 1
            else:
                result = mid
                max_rate = mid - 1
        return result
                                
                