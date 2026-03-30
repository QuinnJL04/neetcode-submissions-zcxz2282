class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        window = []
        res = []
        #init first window
        for i in range(k):
            window.append(nums[i])

        for r in range(k, len(nums)):
            #append current max of window
            res.append(max(window))
            #slide window
            window.pop(0)
            window.append(nums[r])
        
        res.append(max(window))
        
        return res