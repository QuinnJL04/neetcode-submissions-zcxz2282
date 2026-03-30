class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        res = 0 

        graph = {i: [] for i in range(n)}

        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        visited = set()
        def dfs(node):
            for n in graph[node]:
                if n not in visited:
                    visited.add(n)
                    dfs(n)
        
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                res += 1
    
        return res


