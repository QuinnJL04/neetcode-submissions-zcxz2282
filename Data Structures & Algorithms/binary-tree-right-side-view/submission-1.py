# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        queue = deque([root])

        while queue:
            level = len(queue)
            for i in range(level):
                curr = queue.popleft()
                if curr is not None:
                    if i == level - 1:
                        res.append(curr.val)
                    if curr.left is not None:
                        queue.append(curr.left)
                    if curr.right is not None:
                        queue.append(curr.right)

        return res
           
        