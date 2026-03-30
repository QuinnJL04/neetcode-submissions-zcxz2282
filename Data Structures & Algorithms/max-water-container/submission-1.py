class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j = len(heights) - 1
        global_max = 0
        for i in range(len(heights)):
            while j > i:
                curr_height = min(heights[i], heights[j])
                local_max = curr_height * (j - i)
                global_max = max(global_max, local_max)
                j-=1
            j = len(heights) - 1
        return global_max