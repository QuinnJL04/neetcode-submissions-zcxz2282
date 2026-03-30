# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        queue1 = deque([p])
        queue2 = deque([q])

        while queue1 and queue2:
            curr1 = queue1.popleft()
            curr2 = queue2.popleft()

            if not curr1 and not curr2:
                continue

            if not curr1 or not curr2:
                return False

            if curr1.val != curr2.val:
                return False

            queue1.append(curr1.left)
            queue2.append(curr2.left)
            queue1.append(curr1.right)
            queue2.append(curr2.right)

        return not queue1 and not queue2

