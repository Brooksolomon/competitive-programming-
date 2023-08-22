class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set()
        def dfs(x):
            visited.add(x)
            if not  set(rooms[x]).difference(visited):
                return
            
            for i in set(rooms[x]).difference(visited):
                dfs(i)
        dfs(0)
        return len(visited) == len(rooms)
