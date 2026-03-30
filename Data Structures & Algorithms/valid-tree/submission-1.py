class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #must have n - 1 edges
        #must be acyclic

        if len(edges) != (n - 1):
            return False

        graph = {i:[] for i in range(n)}

        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        print(graph)
        visit = set()
        def dfs(node, parent):
            if node in visit:
                return False

            visit.add(node)

            for n in graph[node]:
                if n == parent:
                    continue
                if not dfs(n, node):
                    return False
            

            return True

        if not dfs(0, -1):
            return False

        return len(visit) == n