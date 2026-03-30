class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in range(len(matrix)):
            l = 0
            r = len(matrix[row]) - 1
            mid = (l+r)//2
            while l <= r:
                if matrix[row][mid] < target:
                    l = mid + 1
                    mid = (l+r) // 2
                elif matrix[row][mid] > target:
                    r = mid - 1
                    mid = (l+r)//2
                else:
                    return True

        return False