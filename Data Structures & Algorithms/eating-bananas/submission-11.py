class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_rate = 1
        max_rate = max(piles)
        result = max_rate
        while min_rate <= max_rate:
            mid = (min_rate + max_rate) // 2
            curr_time = 0

            for i in range(len(piles)):
                pile = piles[i]
                curr_time += math.ceil(pile / mid)

            if curr_time > h:
                min_rate = mid + 1
            else:
                result = min(result, mid)
                max_rate = mid - 1
        return result
            
