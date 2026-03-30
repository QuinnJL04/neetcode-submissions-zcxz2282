# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        queue = deque([(root, root.val)])

        while queue:
            curr, curr_max = queue.popleft()

            if curr.val >= curr_max:
                count+=1

            curr_max = max(curr_max, curr.val)

            if curr.left is not None:
                queue.append((curr.left, curr_max))
            if curr.right is not None:
                queue.append((curr.right, curr_max))
            
        return count
            
