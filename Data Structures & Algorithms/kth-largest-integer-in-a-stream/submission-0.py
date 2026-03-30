import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #init the lists as a heap minheap
        self.k = k
        h = [] 
        heapq.heapify(h)
        for num in nums:
            heapq.heappush(h, num)
        self.nums = h
        print(f"k = {self.k} and nums = {self.nums}")
        

    def add(self, val: int) -> int:
        # push the new value onto the heap
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]


        
