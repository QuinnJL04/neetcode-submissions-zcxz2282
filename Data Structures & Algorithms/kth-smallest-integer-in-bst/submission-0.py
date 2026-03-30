import heapq
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        h = []
        heapq.heapify(h)

        queue = deque([root])

        while queue:
            curr = queue.popleft()
            heapq.heappush(h, curr.val)
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
        res = 0
        for i in range(k):
            res = heapq.heappop(h)

        return res
        

            