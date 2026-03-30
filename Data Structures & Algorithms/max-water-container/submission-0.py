class Solution:
    def maxArea(self, heights: List[int]) -> int:
        total_area = 0
        i = 0
        j = len(heights) - 1

        #(j - i) * min(heights[i], heights[j])
        while i < j:

            area = (j - i) * min(heights[i], heights[j])
            print(area)
            total_area = max(total_area, area)

            if i < j and heights[i] > heights[j]:
                j-=1
            elif i < j and heights[j] > heights[i]:
                i+=1
            else:
                i+=1
                j-=1


        return total_area