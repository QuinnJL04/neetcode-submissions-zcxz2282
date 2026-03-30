class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        window = []
        res = []
        #init first window
        for i in range(k):
            window.append(nums[i])

        l = 0
        for r in range(k, len(nums)):
            #append current max of window
            res.append(max(window))
            #slide window
            print(l)
            window.pop(0)
            l += 1
            window.append(nums[r])
        
        res.append(max(window))
        
        return res