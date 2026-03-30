class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        global_max = 0
        
        while i < j:
            curr_height = min(heights[i], heights[j])
            local_max = curr_height * (j - i)
            global_max = max(global_max, local_max)

            if i < j and heights[i] > heights[j]:
                j-=1
            elif i < j and heights[j] > heights[i]:
                i+=1
            else:
                i+=1
                j-=1
        return global_max