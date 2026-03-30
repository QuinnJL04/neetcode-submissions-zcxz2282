# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        cnt = k
        res = root.val

        def inorderDFS(node):

            nonlocal cnt, res
            
            if not node:
                return 

            inorderDFS(node.left)

            print(node.val)

            cnt -= 1
            if cnt == 0:
                res = node.val
                return

            inorderDFS(node.right)
        
        inorderDFS(root)
        return res