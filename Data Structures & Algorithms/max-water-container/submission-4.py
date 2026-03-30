class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1
        res = 0
        while l < r:
            height = min(heights[l], heights[r])
            curr_water = height * (r - l)
            res = max(res, curr_water)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res

