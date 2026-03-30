# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def compare(q1, q2):

            while q1 and q2:
                curr1 = q1.popleft()
                curr2 = q2.popleft()

                if not curr1 and not curr2:
                    continue

                if not curr1 or not curr2:
                    return False

                if curr1.val != curr2.val:
                    return False

                #add the left node
                q1.append(curr1.left)
                q2.append(curr2.left)
                #add the right node
                q1.append(curr1.right)
                q2.append(curr2.right)

            return not q1 and not q2

        queue = deque([root])


        while queue:
            curr = queue.popleft()

            if curr and curr.val == subRoot.val:
                if compare(deque([curr]), deque([subRoot])):
                    return True

            if curr.left:
                queue.append(curr.left)
            
            if curr.right:
                queue.append(curr.right)

        return False
