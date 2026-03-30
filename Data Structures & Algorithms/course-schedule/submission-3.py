class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            graph[crs].append(pre)

        visiting = set()
        done = set()

        def dfs(crs):
            if crs in visiting:   # cycle
                return False
            if crs in done:       # already checked, safe
                return True

            visiting.add(crs)
            for pre in graph[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)

            done.add(crs)         # mark safe
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
