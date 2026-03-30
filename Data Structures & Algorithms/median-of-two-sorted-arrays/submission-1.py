class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            cut1 = (left + right) // 2
            cut2 = (m + n + 1) // 2 - cut1

            maxLeft1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            minRight1 = float('inf') if cut1 == m else nums1[cut1]

            maxLeft2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            minRight2 = float('inf') if cut2 == n else nums2[cut2]

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                right = cut1 - 1
            else:
                left = cut1 + 1
