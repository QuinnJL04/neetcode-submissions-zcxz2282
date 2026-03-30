class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #area is distacne between bars * lower bound height

        l = 0
        r = len(heights) - 1
        result = 0
        while l <= r:

            distance = r - l 
            area = distance * min(heights[l], heights[r])
            if heights[l] > heights[r]:
                r-=1
            elif heights[r] > heights[l]:
                l+=1
            else:
                l+=1
                r-=1
            result = max(result, area)
        return result