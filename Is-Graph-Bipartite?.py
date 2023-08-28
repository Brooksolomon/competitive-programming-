class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        odd  = [0] * len(graph)
        def bfs(i):
            if odd[i]:
                return True 
            queue = deque([i])
            odd[i] = -1
            while queue:
                i = queue.popleft()
                for n in graph[i]:
                    if odd[i] == odd[n]:
                        return False 
                    elif not odd[n]:
                        queue.append(n)
                        odd[n] = -1 * odd[i]
            return True

        for x in range(len(graph)):
            if not bfs(x):
                print(x)
                return False
        return True 
