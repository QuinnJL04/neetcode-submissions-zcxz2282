class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        min_rate = 1
        max_rate = max(piles)
        result = max_rate
        while min_rate <= max_rate:
            eating_rate = (min_rate + max_rate) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / eating_rate)
            
            if time > h:
                min_rate = eating_rate + 1
            else:
                result = min(result, eating_rate)
                max_rate = eating_rate - 1
        return result
