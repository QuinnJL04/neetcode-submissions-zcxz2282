"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        cloned = {}
        cloned[node] = Node(node.val)
        queue = deque([node])

        while queue:
            curr_node = queue.popleft()

            for neighbor in curr_node.neighbors:
                if neighbor not in cloned:
                    queue.append(neighbor)
                    cloned[neighbor] = Node(neighbor.val)
                cloned[curr_node].neighbors.append(cloned[neighbor])
            
        return cloned[node]
                


        