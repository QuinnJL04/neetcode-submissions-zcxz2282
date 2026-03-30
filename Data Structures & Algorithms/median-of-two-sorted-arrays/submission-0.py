class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        #if odd return middle else return sum(i, j) / 2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        l = 0
        r = len(nums1)
        
        while l <= r:
            m = (l + r) // 2
            j = ((len(nums1) + len(nums2) + 1) // 2) - m

            maxLeft1 = float('-inf') if m == 0 else nums1[m - 1]
            maxRight1 = float('inf') if m == len(nums1) else nums1[m]
            maxLeft2 = float('-inf') if j == 0 else nums2[j - 1]
            maxRight2 = float('inf') if j == len(nums2) else nums2[j]

            if maxLeft1 <= maxRight2 and maxLeft2 <= maxRight1:
                if ((len(nums1) + len(nums2)) % 2) == 0:
                    return (max(maxLeft1, maxLeft2) + min(maxRight1, maxRight2)) / 2
                else:
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > maxRight2:
                r = m - 1
            else:
                l = m + 1



