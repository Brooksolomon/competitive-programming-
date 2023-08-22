class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        goal = [len(grid) - 1, len(grid) - 1]
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        mini = float('inf')
        queue = deque()
        queue.append((0, 0, 1))
        visited = set()
        while queue:
            for i in range(len(queue)):
                cur = queue.popleft()
                x = cur[0]
                y = cur[1]
                if (x,y) in visited:
                    continue
                visited.add((x,y))
                if x < 0 or y < 0 or x > len(grid) - 1 or y > len(grid[0]) - 1 or grid[x][y] == 1:
                    continue
                if [x,y] == goal:
                    mini = min(mini, cur[2])
                    continue
                for j in direction:
                    queue.append((x + j[0], y + j[1], cur[2] + 1))
        if mini==float('inf') :return -1
        return mini
        


    
        
